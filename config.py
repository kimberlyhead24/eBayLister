from dotenv import load_dotenv
import os

load_dotenv()

AUTH_EBAY =os.getenv("AUTH_EBAY", "your_auth_ebay_here")
KEY_EBAY = os.getenv("KEY_EBAY", "your_key_ebay_here")
EBAY_APP_ID = os.getenv("EBAY_APP_ID", "your_ebay_app_id_here")
AZURE_STORAGE_CONNECTION_STRING = os.getenv(
    "AZURE_STORAGE_CONNECTION_STRING",
    "your_azure_storage_here"
)

APP_ENV = os.getenv("APP_ENV", "development")
APP_HOST = os.getenv("APP_HOST", "127.0.0.1")
APP_PORT = int(os.getenv("APP_PORT", "8000"))