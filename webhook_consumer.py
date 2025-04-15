import hashlib
import json
from typing import Any, Dict
import logging
import http
import hmac

from constants import *
from ekacare import EkaCareClient


logger = logging.getLogger(__name__)

# Implement your logic of allowing selective payloads
ALLOWED_PAYLOADS = ["appointment.created", "appointment.updated"]


def force_bytes(s, encoding='utf-8'):
    if isinstance(s, bytes):
        return s
    return str(s).encode(encoding)


class WebhookConsumer:
    """
    This class handles the webhook for appointment events.
    Implement you logic to handle webhook data here
    """

    def __init__(self, payload: Dict[Any, Any] = None):
        self.payload = payload or {}


    def verify_signature(self, signature_header):
        """
        Verify the signature of the request.
        """

        body_str = json.dumps(self.payload, separators=(',', ':'))
        print(f"body_str: {body_str}")
        if not signature_header:
            return False, 'Missing signature'

        logger.debug(f"Received signature_header: {signature_header}, body: {body_str}")

        try:
            signature_parts = dict(item.split('=') for item in signature_header.split(','))
            timestamp = signature_parts['t']
            signature = signature_parts['v1']
        except Exception as e:
            logger.error(f"Error parsing signature header: {signature_header}, body: {body_str}")
            return False, 'Invalid signature format'

        logger.debug(f"Extracted signature parts: timestamp: {timestamp}, signature: {signature}, body: {body_str}")

        signed_payload = f"{timestamp}.{body_str}"
        expected_signature = hmac.new(
            key=force_bytes(SIGNING_KEY),
            msg=force_bytes(signed_payload),
            digestmod=hashlib.sha256
        ).hexdigest()

        logger.debug(f"Expected signature: {expected_signature}, Received: {signature}, body: {body_str}")

        if not hmac.compare_digest(expected_signature, signature):
            logger.info(
                f"Signature mismatch. Expected signature: {expected_signature}, "
                f"Received: {signature}, "
                f"body: {body_str}"
            )
            return False, 'Invalid signature'

        return True, None

    def get_data(self, client_id: str, client_secret: str, api_key: str) -> dict[str, str] | dict[str, str] | dict[
        str, str] | dict[str, str] | str | dict[str, str]:
        """
        Print the webhook data.

        Args:
            data (dict): The data received from the webhook.
            :param body:
            :param client_id:
            :param api_key:
            :param client_secret:
        """

        if api_key:
            client = EkaCareClient(
                client_id=client_id,
                client_secret=client_secret,
                api_key=api_key,
            )
        else:
            client = EkaCareClient(
                client_id=client_id,
                client_secret=client_secret,
            )

        if self.payload.get("event") in ALLOWED_PAYLOADS:

            # Get data from appointment payload
            appointment_id = self.payload.get("data", {}).get("appointment_id")
            patient_id = self.payload.get("data", {}).get("patient_id")
            clinic_id = self.payload.get("data", {}).get("clinic_id")
            doctor_id = self.payload.get("data", {}).get("doctor_id")

            if not appointment_id:
                logger.error("Missing appointment_id in payload")
                return {"error": "Missing appointment_id in payload"}
            if not patient_id:
                logger.error("Missing patient_id in payload")
                return {"error": "Missing patient_id in payload"}
            if not clinic_id:
                logger.error("Missing clinic_id in payload")
                return {"error": "Missing clinic_id in payload"}
            if not doctor_id:
                logger.error("Missing doctor_id in payload")
                return {"error": "Missing doctor_id in payload"}


            logger.debug(f"Webhook data for appointment {self.payload}:")
            return_payload = {"appointment_details": client.appointments.get_appointment_details(
                appointment_id), "patient_details": client.patient.get_patient(patient_id),
                              "clinic_details": client.clinic_doctor.get_clinic_details(clinic_id),
                              "doctor_details": client.clinic_doctor.get_doctor_details(doctor_id)}
            return json.dumps(return_payload)

        else:
            return {"error": "payload not supported, allowed payloads are " + str(ALLOWED_PAYLOADS)}


