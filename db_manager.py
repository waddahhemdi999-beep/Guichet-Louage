"""Database manager for SQLite operations."""

import sqlite3
import os
from typing import List, Optional, Dict, Any
from datetime import datetime


class DatabaseManager:
    """Manages SQLite database operations for Louage booking system."""
    
    def __init__(self, db_path: str = "louage_booking.db"):
        """Initialize database manager."""
        self.db_path = db_path
        self.connection: Optional[sqlite3.Connection] = None
        self.init_database()
    
    def connect(self) -> None:
        """Establish database connection."""
        if not self.connection:
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row
    
    def disconnect(self) -> None:
        """Close database connection."""
        if self.connection:
            self.connection.close()
            self.connection = None
    
    def init_database(self) -> None:
        """Initialize database with tables."""
        self.connect()
        cursor = self.connection.cursor()
        
        # Routes table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS routes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                departure_city TEXT NOT NULL,
                arrival_city TEXT NOT NULL,
                departure_time TEXT NOT NULL,
                arrival_time TEXT NOT NULL,
                distance_km REAL,
                price REAL NOT NULL,
                duration_hours REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Buses table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS buses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                registration_number TEXT UNIQUE NOT NULL,
                capacity INTEGER DEFAULT 8,
                current_passengers INTEGER DEFAULT 0,
                route_id INTEGER,
                driver_name TEXT,
                phone_number TEXT,
                status TEXT DEFAULT 'available',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (route_id) REFERENCES routes(id)
            )
        """)
        
        # Passengers table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS passengers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                phone_number TEXT NOT NULL,
                id_number TEXT UNIQUE NOT NULL,
                email TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Bookings table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                passenger_id INTEGER NOT NULL,
                bus_id INTEGER NOT NULL,
                route_id INTEGER NOT NULL,
                seat_number INTEGER NOT NULL,
                booking_date TIMESTAMP,
                departure_date TEXT NOT NULL,
                status TEXT DEFAULT 'confirmed',
                payment_status TEXT DEFAULT 'pending',
                amount REAL NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (passenger_id) REFERENCES passengers(id),
                FOREIGN KEY (bus_id) REFERENCES buses(id),
                FOREIGN KEY (route_id) REFERENCES routes(id)
            )
        """)
        
        self.connection.commit()
    
    def execute_query(self, query: str, params: tuple = ()) -> List[Dict[str, Any]]:
        """Execute SELECT query and return results."""
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return [dict(row) for row in cursor.fetchall()]
    
    def execute_update(self, query: str, params: tuple = ()) -> int:
        """Execute INSERT/UPDATE/DELETE query and return row count."""
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor.rowcount
    
    def close(self) -> None:
        """Close database connection."""
        self.disconnect()
