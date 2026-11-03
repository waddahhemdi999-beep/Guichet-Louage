"""Booking model for seat reservations."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Booking:
    """Represents a booking/reservation for a Louage seat."""
    
    id: Optional[int] = None
    passenger_id: int = 0
    bus_id: int = 0
    route_id: int = 0
    seat_number: int = 0
    booking_date: Optional[datetime] = None
    departure_date: str = ""  # Format: "YYYY-MM-DD"
    status: str = "confirmed"  # confirmed, cancelled, completed
    payment_status: str = "pending"  # pending, paid, refunded
    amount: float = 0.0
    created_at: Optional[datetime] = None
    
    def __str__(self) -> str:
        return f"Booking #{self.id} - Seat {self.seat_number} ({self.status})"
