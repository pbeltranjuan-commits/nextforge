from cryptography.fernet import Fernet
from .config import settings

fernet = Fernet(settings.ENCRYPTION_KEY.encode())

def encrypt(key: str) -> str:
    return fernet.encrypt(key.encode()).decode()

def decrypt(token: str) -> str:
    return fernet.decrypt(token.encode()).decode()

def mask_key(key: str) -> str:
    return key[:4] + "****" + key[-4:]
