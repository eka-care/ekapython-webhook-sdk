# EkaCare Webhook SDK

## Overview
The EkaCare Webhook SDK processes appointment events through webhooks, validates webhook signatures, and handles appointment data securely.

## Environment Variables

The following environment variables need to be set for the application to function properly:

### Mandatory Variables
- `CLIENT_ID`: Your client ID for authentication (required in all cases)
- `CLIENT_SECRET`: Your client secret for authentication (required in all cases)

### Conditional Variables
- `SIGNING_KEY`: 
  - **Required** when `IS_SIGNING_KEY_IMPLEMENTED` is set to `True` in `constants.py`
  - Used for verifying webhook signatures

- `API_KEY`: 
  - **Required** for business use cases
  - Used for making authorized API calls to the EkaCare services

### Configuration
If you need to disable signature verification, you can set `IS_SIGNING_KEY_IMPLEMENTED = False` in the `constants.py` file.

Make sure to properly set these environment variables before deploying or running the application.

## Configuration

### Signature Verification
The SDK supports signature verification to ensure webhook security:

1. In `constants.py`, set `IS_SIGNING_KEY_IMPLEMENTED`:
   - `True`: Enable signature verification (recommended for production)
   - `False`: Disable signature verification (use only for testing)

```python
import os

# Set to True if you want to implement signature verification
IS_SIGNING_KEY_IMPLEMENTED = True

# Provide signing key here
SIGNING_KEY = os.getenv("SIGNING_KEY")

# Client ID (Mandatory)
CLIENT_ID = os.getenv("CLIENT_ID")

# Client Secret (Mandatory)
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# Api Key (Optional, Required when you need to represent use case for business id)
API_KEY = os.getenv("API_KEY")

