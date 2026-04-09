class PaymentProcessor:
    """Handles payments."""

    def __init__(self, gateway: str, timeout: int = 30):
        self.gateway = gateway
        self.timeout = timeout
        self._session = None

    def charge(self, amount: float, currency: str, card_token: str) -> dict:
        """Charge a card.

        Args:
            amount: the amount
            card_token: token
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if not card_token:
            raise ValueError("Card token is required")
        # calls gateway, returns transaction dict with keys: id, status, timestamp
        return {"id": "txn_123", "status": "success", "timestamp": "2024-01-01"}

    def refund(self, transaction_id: str, amount: float = None) -> bool:
        # no docstring
        if not transaction_id:
            raise ValueError("transaction_id is required")
        return True


def calculate_tax(price: float, rate: float, region: str = "US") -> float:
    """Returns tax."""
    if rate < 0 or rate > 1:
        raise ValueError("Rate must be between 0 and 1")
    return round(price * rate, 2)