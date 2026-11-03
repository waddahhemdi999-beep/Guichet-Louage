"""Main entry point for Louage Booking Application."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from louage_app.ui import MainWindow


def main():
    """Run the application."""
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
