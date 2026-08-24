import os
from dotenv import load_dotenv


def load_env():
    """Load environment variables from the .env file in the project root."""
    load_dotenv()


def get_key(name: str) -> str:
    """Return the value of an environment variable, raising a clear error if missing."""
    value = os.getenv(name)
    if value is None:
        raise ValueError(f"Missing environment variable: {name}")
    return value
