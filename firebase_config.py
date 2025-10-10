import firebase_admin
from firebase_admin import credentials, firestore
from django.conf import settings

SERVICE_ACCOUNT_PATH = settings.FIREBASE_SERVICE_ACCOUNT_PATH

# Check the file exists
import os
if not os.path.exists(SERVICE_ACCOUNT_PATH):
    raise RuntimeError(f"Firebase service account not found at {SERVICE_ACCOUNT_PATH}")

cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
firebase_admin.initialize_app(cred)
db = firestore.client()
