"""Passenger model for booking system."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Passenger:
    """Represents a passenger booking a Louage seat."""
    
    id: Optional[int] = None
    full_name: str = ""
    phone_number: str = ""
    id_number: str = ""
    email: Optional[str] = None
    created_at: Optional[datetime] = None
    
    def __str__(self) -> str:
        return f"{self.full_name} ({self.phone_number})"
