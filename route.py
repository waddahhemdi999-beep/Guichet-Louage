"""Route model for Louage routes."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Route:
    """Represents a Louage route with departure and arrival information."""
    
    id: Optional[int] = None
    departure_city: str = ""
    arrival_city: str = ""
    departure_time: str = ""  # Format: "HH:MM"
    arrival_time: str = ""  # Format: "HH:MM"
    distance_km: float = 0.0
    price: float = 0.0
    duration_hours: float = 0.0
    created_at: Optional[datetime] = None
    
    def __str__(self) -> str:
        return f"{self.departure_city} → {self.arrival_city} ({self.departure_time})"
