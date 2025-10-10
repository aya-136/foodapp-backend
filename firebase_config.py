import os
import json
import firebase_admin
from firebase_admin import credentials, firestore

# Try to load from environment variable
firebase_creds_json = os.getenv("FIREBASE_SERVICE_ACCOUNT")

if firebase_creds_json:
    # Parse the JSON string from the environment variable
    firebase_creds = json.loads(firebase_creds_json)
    cred = credentials.Certificate(firebase_creds)
    firebase_admin.initialize_app(cred)
    db = firestore.client()
else:
    SERVICE_ACCOUNT_PATH = os.path.join(
        os.path.dirname(__file__), "service-account.json"
    )
    if os.path.exists(SERVICE_ACCOUNT_PATH):
        cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
    else:
        raise RuntimeError("Firebase service account not found (env var or local file)")
