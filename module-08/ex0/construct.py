"""Exercise 0: Entering the Matrix - virtual environment detection."""
from __future__ import annotations

import os
import site
import sys
from typing import Dict, List, Optional


def is_in_virtual_env() -> bool:
    """Return True if running inside a virtual environment."""
    return sys.prefix != getattr(sys, "base_prefix", sys.prefix)


def get_env_name() -> Optional[str]:
    """Best-effort derivation of the venv name from the prefix path."""
    try:
        return os.path.basename(sys.prefix)
    except Exception:
        return None


def collect_environment_info() -> Dict[str, Optional[str | List[str]]]:
    """Gather key environment details safely."""
    try:
        venv = is_in_virtual_env()
        info: Dict[str, Optional[str | List[str]]] = {
            "python_executable": sys.executable,
            "venv_name": get_env_name() if venv else None,
            "venv_prefix": sys.prefix if venv else None,
            "site_packages": site.getsitepackages(),
        }
        return info
    except Exception as exc:  # pragma: no cover - defensive
        return {"error": str(exc)}


def print_outside_matrix(info: Dict[str, Optional[str | List[str]]]) -> None:
    print("Outside the Matrix")
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {info.get('python_executable')}")
    print("Virtual Environment: None detected")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\\Scripts\\activate   # On Windows")
    print("Then run this program again.")


def print_inside_construct(info: Dict[str, Optional[str | List[str]]]) -> None:
    print("Inside the Construct")
    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {info.get('python_executable')}")
    print(f"Virtual Environment: {info.get('venv_name')}")
    print(f"Environment Path: {info.get('venv_prefix')}")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print("Package installation paths:")
    for path in info.get("site_packages", []) or []:
        print(path)


def main() -> None:
    info = collect_environment_info()
    if "error" in info:
        print("Error inspecting environment:", info["error"])
        return

    if is_in_virtual_env():
        print_inside_construct(info)
    else:
        print_outside_matrix(info)


if __name__ == "__main__":
    main()
