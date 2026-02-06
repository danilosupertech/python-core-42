"""Exercise 2: Accessing the Mainframe - environment configuration."""
from __future__ import annotations

import os
from typing import Dict, Optional


def load_env_file() -> bool:
    """Load .env using python-dotenv if available; return True if loaded."""
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("[WARN] python-dotenv not installed. Skipping .env load. Install with pip install python-dotenv")
        return False
    loaded = load_dotenv()
    return bool(loaded)


def read_config() -> Dict[str, Optional[str]]:
    """Read configuration from environment variables."""
    vars_needed = ["MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"]
    config: Dict[str, Optional[str]] = {}
    for var in vars_needed:
        config[var] = os.getenv(var)
    return config


def describe_config(config: Dict[str, Optional[str]]) -> None:
    """Display the current configuration settings."""
    mode = config.get("MATRIX_MODE") or "development"
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {('Connected' if config.get('DATABASE_URL') else 'Missing DATABASE_URL')}")
    print(f"API Access: {'Authenticated' if config.get('API_KEY') else 'Missing API_KEY'}")
    print(f"Log Level: {config.get('LOG_LEVEL') or 'DEFAULT'}")
    print(f"Zion Network: {config.get('ZION_ENDPOINT') or 'Missing ZION_ENDPOINT'}")


def security_check(config: Dict[str, Optional[str]]) -> None:
    """Perform security validation of environment configuration."""
    print("Environment security check:")
    if not config.get("API_KEY"):
        print("[WARN] Missing API_KEY. Do not hardcode secrets; set via env or .env.")
    else:
        print("[OK] API_KEY provided via environment.")

    if os.path.exists(".env"):
        print("[OK] .env file present (should be gitignored).")
    else:
        print("[INFO] No .env file found; using environment variables only.")

    print("[OK] Production overrides available via environment variables.")


def main() -> None:
    """Main entry point for environment configuration management."""
    print("ORACLE STATUS: Reading the Matrix...")
    load_env_file()
    config = read_config()
    describe_config(config)
    security_check(config)


if __name__ == "__main__":
    main()
