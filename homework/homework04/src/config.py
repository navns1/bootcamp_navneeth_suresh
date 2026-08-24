import os
from dotenv import load_dotenv


def load_env():
    """Load environment variables from the .env file in the project root."""
    load_dotenv()


def get_key(name: str, required: bool = True) -> str:
    """
    Return the value of an environment variable.

    If required=True and the variable is missing, raises an error.
    If required=False and the variable is missing, returns None instead
    of raising, useful for optional keys (e.g. sources that don't need one).
    """
    value = os.getenv(name)
    if value is None and required:
        raise ValueError(f"Missing environment variable: {name}")
    return value
