# EkaCare Webhook SDK

## Overview
The EkaCare Webhook SDK processes appointment events through webhooks, validates webhook signatures, and handles appointment data securely.

## Configuration

### Signature Verification
The SDK supports signature verification to ensure webhook security:

1. In `constants.py`, set `IS_SIGNING_KEY_IMPLEMENTED`:
   - `True`: Enable signature verification (recommended for production)
   - `False`: Disable signature verification (use only for testing)

```python
# Enable signature verification
IS_SIGNING_KEY_IMPLEMENTED = True