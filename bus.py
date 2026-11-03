"""Bus/Vehicle model for Louage operations."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Bus:
    """Represents a Louage bus/vehicle."""
    
    id: Optional[int] = None
    registration_number: str = ""
    capacity: int = 8  # Standard Louage capacity
    current_passengers: int = 0
    route_id: Optional[int] = None
    driver_name: str = ""
    phone_number: str = ""
    status: str = "available"  # available, in_transit, full
    created_at: Optional[datetime] = None
    
    @property
    def available_seats(self) -> int:
        """Calculate available seats."""
        return self.capacity - self.current_passengers
    
    @property
    def is_full(self) -> bool:
        """Check if bus is full."""
        return self.current_passengers >= self.capacity
    
    def __str__(self) -> str:
        return f"Bus {self.registration_number} ({self.current_passengers}/{self.capacity})"
