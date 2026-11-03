"""Main application window for Louage booking system using Tkinter."""

import os
import sys
import tempfile
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from louage_app.database import DatabaseManager

HOME_CITY = "السبيخة"
DESTINATION_CITIES = ["القيروان", "الفحص", "تونس", "سوسة"]
TICKET_WIDTH = 420
TICKET_HEIGHT = 600
TICKET_MARGIN = 10
TICKET_TEXT_POSITIONS = {
    "destination": (210, 115),
    "date": (210, 325),
    "seats": (210, 405),
    "unit_price": (210, 455),
    "price": (210, 515),
}
class MainWindow(tk.Tk):
    """Main application window."""

    def __init__(self):
        """Initialize main window."""
        super().__init__()
        self.db_manager = DatabaseManager()
        self.title("محطة اللواجات بالسبيخة")
        self.geometry("1100x650")

        style = ttk.Style()
        style.theme_use('clam')

        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=12, pady=12)

        title_label = ttk.Label(main_frame, text="محطة اللواجات بالسبيخة", font=("Arial", 18, "bold"))
        title_label.pack(pady=(0, 12))

        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.booking_tab = self.create_booking_tab()
        self.notebook.add(self.booking_tab, text="حجز تذكرة")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_booking_tab(self) -> ttk.Frame:
        """Create the booking ticket interface."""
        tab = ttk.Frame(self.notebook, padding=12)

        left_panel = ttk.Frame(tab)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 12))

        form_frame = ttk.LabelFrame(left_panel, text="تفاصيل الرحلة", padding=12)
        form_frame.pack(fill=tk.X, pady=(0, 10))

        ttk.Label(form_frame, text="من:").grid(row=0, column=0, sticky=tk.E, pady=5)
        self.departure_city = ttk.Combobox(form_frame, width=30, state="readonly", values=[HOME_CITY])
        self.departure_city.set(HOME_CITY)
        self.departure_city.grid(row=0, column=1, pady=5, padx=(10, 0))

        ttk.Label(form_frame, text="إلى:").grid(row=1, column=0, sticky=tk.E, pady=5)
        self.arrival_city = ttk.Combobox(form_frame, width=30, state="readonly", values=DESTINATION_CITIES)
        self.arrival_city.set(DESTINATION_CITIES[0])
        self.arrival_city.grid(row=1, column=1, pady=5, padx=(10, 0))

        ttk.Label(form_frame, text="تاريخ السفر:").grid(row=2, column=0, sticky=tk.E, pady=5)
        self.departure_date = ttk.Entry(form_frame, width=32)
        self.departure_date.insert(0, str(date.today()))
        self.departure_date.grid(row=2, column=1, pady=5, padx=(10, 0))

        ttk.Label(form_frame, text="عدد المقاعد:").grid(row=3, column=0, sticky=tk.E, pady=5)
        self.seats_var = tk.StringVar(value="1")
        seats_spinbox = ttk.Spinbox(form_frame, from_=1, to=20, textvariable=self.seats_var, width=30)
        seats_spinbox.grid(row=3, column=1, pady=5, padx=(10, 0))
        seats_spinbox.bind('<KeyRelease>', self.on_seats_change)

        button_frame = ttk.Frame(left_panel)
        button_frame.pack(fill=tk.X, pady=8)

        ticket_btn = ttk.Button(button_frame, text="إنشاء التذكرة", command=self.create_ticket)
        ticket_btn.pack(side=tk.LEFT)

        # Price map with base price per seat (in TND)
        self.route_price_map = {
            "القيروان": 3300,
            "الفحص": 5200,
            "تونس": 11500,
            "سوسة": 7000,
        }

        right_panel = ttk.Frame(tab)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        ticket_frame = ttk.LabelFrame(right_panel, text="معاينة التذكرة", padding=12)
        ticket_frame.pack(fill=tk.BOTH, expand=True)

        self.ticket_canvas = tk.Canvas(ticket_frame, width=TICKET_WIDTH, height=TICKET_HEIGHT, bg="white", highlightthickness=1, highlightbackground="#cccccc")
        self.ticket_canvas.pack(fill=tk.BOTH, expand=True)

        self.ticket_image = None

        self.ticket_route = ""
        self.ticket_date = ""
        self.ticket_price = ""
        self.ticket_seats = 1

        # Bind events to update preview
        self.departure_city.bind('<<ComboboxSelected>>', self.update_ticket_preview)
        self.arrival_city.bind('<<ComboboxSelected>>', self.update_ticket_preview)
        self.departure_date.bind('<KeyRelease>', self.update_ticket_preview)

        self.update_ticket_preview()

        return tab

    def on_seats_change(self, event=None):
        """Handle seats value change."""
        self.update_ticket_preview()

    def get_seats(self):
        """Return the selected number of seats within the allowed range."""
        try:
            seats = int(self.seats_var.get())
        except (tk.TclError, ValueError):
            return 1
        return max(1, min(seats, 20))

    def render_ticket_template(self):
        """Render the built-in ticket and overlay route details onto it."""
        self.ticket_canvas.delete("all")
        self.ticket_canvas.create_rectangle(TICKET_MARGIN, TICKET_MARGIN, TICKET_WIDTH - TICKET_MARGIN, TICKET_HEIGHT - TICKET_MARGIN, outline="#999999", fill="#f7f7f7")

        destination_text = self.ticket_route if self.ticket_route else "الوجهة: -"
        seats_text = f"عدد المقاعد: {self.ticket_seats}"
        unit_price_text = f"سعر المقعد: {self.ticket_unit_price}"
        price_text = self.ticket_price if self.ticket_price else "المبلغ الجملي: -"
        date_text = self.ticket_date if self.ticket_date else "التاريخ: -"

        self.ticket_canvas.create_text(
            TICKET_TEXT_POSITIONS["destination"][0],
            TICKET_TEXT_POSITIONS["destination"][1],
            text=destination_text,
            fill="#111111",
            font=("Arial", 15, "bold"),
            anchor=tk.CENTER,
        )
        self.ticket_canvas.create_text(
            TICKET_TEXT_POSITIONS["date"][0],
            TICKET_TEXT_POSITIONS["date"][1],
            text=date_text,
            fill="#111111",
            font=("Arial", 12),
            anchor=tk.CENTER,
        )
        self.ticket_canvas.create_text(
            TICKET_TEXT_POSITIONS["seats"][0],
            TICKET_TEXT_POSITIONS["seats"][1],
            text=seats_text,
            fill="#111111",
            font=("Arial", 12),
            anchor=tk.CENTER,
        )
        self.ticket_canvas.create_text(
            TICKET_TEXT_POSITIONS["unit_price"][0],
            TICKET_TEXT_POSITIONS["unit_price"][1],
            text=unit_price_text,
            fill="#111111",
            font=("Arial", 12),
            anchor=tk.CENTER,
        )
        self.ticket_canvas.create_text(
            TICKET_TEXT_POSITIONS["price"][0],
            TICKET_TEXT_POSITIONS["price"][1],
            text=price_text,
            fill="#111111",
            font=("Arial", 14, "bold"),
            anchor=tk.CENTER,
        )

    def update_ticket_preview(self, event=None):
        """Refresh the ticket preview from the selected destination and date."""
        departure = self.departure_city.get().strip() or "-"
        arrival = self.arrival_city.get().strip() or "-"
        departure_date = self.departure_date.get().strip() or str(date.today())
        
        seats = self.get_seats()
        self.ticket_seats = seats

        if arrival in self.route_price_map:
            base_price = self.route_price_map[arrival]
            total_price = base_price * seats
            unit_price = f"{base_price:,} دينار"
            price = f"المبلغ الجملي: {total_price:,} دينار"
        else:
            unit_price = "-"
            price = "المبلغ الجملي: -"

        self.ticket_route = f"المسار: {departure} ← {arrival}"
        self.ticket_price = price
        self.ticket_unit_price = unit_price
        self.ticket_date = f"التاريخ: {departure_date}"
        self.render_ticket_template()

    def create_ticket(self):
        """Create a ticket preview without saving it to a management database."""
        departure = self.departure_city.get().strip()
        arrival = self.arrival_city.get().strip()
        departure_date = self.departure_date.get().strip() or str(date.today())
        
        seats = self.get_seats()

        if not departure or not arrival:
            messagebox.showwarning("بيانات ناقصة", "يرجى اختيار مكان الانطلاق والوجهة.")
            return

        if departure == arrival:
            messagebox.showwarning("مسار غير صالح", "لا يمكن أن يكون مكان الانطلاق والوجهة متطابقين.")
            return

        if arrival not in self.route_price_map:
            messagebox.showwarning("وجهة غير متوفرة", "اختر إحدى الوجهات المتوفرة: القيروان، الفحص، تونس، سوسة.")
            return

        base_price = self.route_price_map[arrival]
        total_price = base_price * seats
        self.update_ticket_preview()
        self.print_ticket(departure, arrival, departure_date, seats, base_price, total_price)
        messagebox.showinfo(
            "التذكرة جاهزة",
            f"من: {departure}\n"
            f"إلى: {arrival}\n"
            f"التاريخ: {departure_date}\n"
            f"عدد المقاعد: {seats}\n"
            f"سعر المقعد: {base_price:,} دينار\n"
            f"المبلغ الجملي: {total_price:,} دينار\n"
            "الحالة: جاهزة للصعود",
        )

    def print_ticket(self, departure, arrival, departure_date, seats, base_price, total_price):
        """Send the created ticket to the default Windows printer."""
        ticket_text = (
            "تذكرة لواج\n"
            "==============================\n"
            f"من: {departure}\n"
            f"إلى: {arrival}\n"
            f"التاريخ: {departure_date}\n"
            f"عدد المقاعد: {seats}\n"
            f"سعر المقعد: {base_price:,} دينار\n"
            f"المبلغ الجملي: {total_price:,} دينار\n"
            "الحالة: جاهزة للصعود\n"
            "==============================\n"
        )

        try:
            with tempfile.NamedTemporaryFile(
                mode="w",
                encoding="utf-8",
                suffix=".txt",
                prefix="louage_ticket_",
                delete=False,
            ) as ticket_file:
                ticket_file.write(ticket_text)

            if os.name != "nt":
                messagebox.showwarning(
                    "Printing unavailable",
                    "Automatic printing is currently supported on Windows only."
                )
                return

            os.startfile(ticket_file.name, "print")
        except OSError as error:
            messagebox.showerror(
                "Printing failed",
                f"The ticket was created, but it could not be sent to the printer.\n\n{error}"
            )

    def on_closing(self):
        """Handle window close event."""
        self.db_manager.close()
        self.destroy()
