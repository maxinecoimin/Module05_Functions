# Business_Rules.py
# Author: Maxine Coimin

Approval_Limit = 1000


def calculate_total(price: float, quantity: int) -> float:
    """
    Calculate the total cost based on price and quantity.

    Returns:
        float: The total cost including a 7% tax.
    """
    return price * quantity * 1.07


def requires_review(amount: float) -> bool:
    """
    Returns:
        bool: True if the transaction requires review, False otherwise.
    """
    return amount > Approval_Limit


def get_approval_tier(amount: float) -> str:
    """
    Returns:
        str: The approval level required as a string.
    """
    if amount <= 500:
        return "auto"
    elif amount <= 2000:
        return "manager"
    else:
        return "director"


def apply_discount(price: float, percent: float) -> float:
    """
    Returns:
        float: The total price after applying the discount. Percent should be 0-100.
    """
    return price * (1 - percent / 100)
