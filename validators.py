"""Validation utilities for Louage booking system."""

import re


def validate_phone(phone: str) -> bool:
    """
    Validate Tunisian phone number format.
    
    Args:
        phone: Phone number string
        
    Returns:
        True if valid, False otherwise
    """
    # Tunisian phone numbers start with +216 or 0
    pattern = r'^(\+216|0)[0-9]{8}$'
    return bool(re.match(pattern, phone.replace(" ", "")))


def validate_id_number(id_number: str) -> bool:
    """
    Validate Tunisian ID number format.
    
    Args:
        id_number: ID number string
        
    Returns:
        True if valid, False otherwise
    """
    # Tunisian ID numbers are typically 8 digits
    pattern = r'^[0-9]{8}$'
    return bool(re.match(pattern, id_number.replace(" ", "")))


def validate_email(email: str) -> bool:
    """
    Validate email format.
    
    Args:
        email: Email string
        
    Returns:
        True if valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
