from typing import Any, Dict


class WebhookConsumer:
    """
    This class handles the webhook for appointment events.
    """

    def __init__(self, payload: Dict[Any, Any] = None):
        self.payload = payload or {}


    def print_data(self, data: dict):
        """
        Print the webhook data.

        Args:
            data (dict): The data received from the webhook.
        """
        print(f"Webhook data for appointment {self.appointment_id}:")
        print(data)