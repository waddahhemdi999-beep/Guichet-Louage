# Louage Booking System

A Python desktop application for managing and booking Louage (shared minibus) reservations in Tunisia.

## About Louage

Louage is a popular shared minibus transportation system in Tunisia, commonly used for intercity travel. These minibuses depart when they have enough passengers and travel fixed routes at affordable prices.

## Features

- **Booking Management**: Search and book Louage seats
- **Route Management**: Add and manage Louage routes
- **Bus Management**: Track vehicles, drivers, and capacity
- **Booking Tracking**: View and manage passenger bookings
- **Database Storage**: SQLite database for persistent data

## Project Structure

```
Louaje/
├── louage_app/
│   ├── __init__.py
│   ├── models/              # Data models
│   │   ├── route.py
│   │   ├── bus.py
│   │   ├── passenger.py
│   │   └── booking.py
│   ├── database/            # Database management
│   │   └── db_manager.py
│   ├── ui/                  # User interface
│   │   └── main_window.py
│   └── utils/               # Utility functions
│       └── validators.py
├── main.py                  # Application entry point
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Installation

1. **Clone or create the project directory**:
   ```bash
   cd d:\Projects\Louaje
   ```

2. **Create a Python virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
python main.py
```

The application window will open with tabs for:
- **Make Booking**: Search routes and book seats
- **Routes**: Manage Louage routes
- **Buses**: Manage vehicles and drivers
- **My Bookings**: View and manage bookings

## Dependencies

- **PyQt6**: Modern GUI framework for Python desktop applications
- SQLite: Built-in database (no installation needed)

## Database

The application uses SQLite to store:
- Routes (departure/arrival cities, times, prices)
- Buses (registration, capacity, driver info)
- Passengers (names, contact info, ID numbers)
- Bookings (reservations, seat assignments, payment status)

Database file: `louage_booking.db` (created automatically)

## Future Enhancements

- Real-time route search functionality
- Payment integration (online payment support)
- SMS/Email notifications
- Mobile app version
- Advanced search filters
- Driver earnings reports
- Customer reviews and ratings

## Development

To extend the application:

1. Add new models in `louage_app/models/`
2. Add database queries in `louage_app/database/db_manager.py`
3. Create UI components in `louage_app/ui/`
4. Add validation functions in `louage_app/utils/validators.py`

## License

This project is open source and available for educational purposes.

## Contact

For questions or suggestions about this Louage booking system, please reach out to the development team.
