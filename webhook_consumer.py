import json
from typing import Any, Dict
from ekacare import EkaCareClient

class WebhookConsumer:
    """
    This class handles the webhook for appointment events.
    Implement you logic to handle webhook data here
    """

    def __init__(self, payload: Dict[Any, Any] = None):
        self.payload = payload or {}


    def get_data(self):
        """
        Print the webhook data.

        Args:
            data (dict): The data received from the webhook.
        """

        client_id = 'YOUR_CLIENT_ID'
        client_secret = 'YOUR_CLIENT_SECRET'
        api_key = 'YOUR_API_KEY'

        client = EkaCareClient(
            client_id=client_id,
            client_secret=client_secret,
            api_key=api_key
        )
        print(f"Webhook data for appointment {self.payload}:")
        return_payload = {"appointment_details": client.appointments.get_appointment_details(
            "YOUR_APPOINTMENT_ID"), "patient_details": client.patient.get_patient("YOUR_PATIENT_ID"),
                          "clinic_details": client.clinic_doctor.get_clinic_details("YOUR_CLINIC_ID"),
                          "doctor_details": client.clinic_doctor.get_doctor_details("YOUR_DOCTOR_ID")}

        return json.dumps(return_payload)
