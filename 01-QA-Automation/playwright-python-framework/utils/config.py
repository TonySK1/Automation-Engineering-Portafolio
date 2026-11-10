import os
from dataclasses import dataclass
from urllib.parse import urlparse

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    base_url: str
    default_timeout_ms: int
    navigation_timeout_ms: int


def get_settings() -> Settings:
    base_url = os.getenv("BASE_URL", "https://the-internet.herokuapp.com")

    default_timeout = os.getenv("DEFAULT_TIMEOUT_MS", "10000")

    navigation_timeout = os.getenv("NAVIGATION_TIMEOUT_MS", "30000")

    parsed_url = urlparse(base_url)

    if parsed_url.scheme not in ("http", "https") or not parsed_url.netloc:
        raise ValueError(f"Invalid BASE_URL: {base_url}")

    try:
        default_timeout_ms = int(default_timeout)
        navigation_timeout_ms = int(navigation_timeout)
    except ValueError as exc:
        raise ValueError("Timeout values must be positive") from exc

    return Settings(
        base_url=base_url.rstrip("/"),
        default_timeout_ms=default_timeout_ms,
        navigation_timeout_ms=navigation_timeout_ms,
    )
