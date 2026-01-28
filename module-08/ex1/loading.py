"""Exercise 1: Loading Programs - dependency management demo."""
from __future__ import annotations

import sys
from typing import Dict, List, Tuple

Missing = Tuple[bool, str]


def try_import(module_name: str) -> Missing:
    try:
        module = __import__(module_name)
        version = getattr(module, "__version__", "unknown")
        return False, f"[OK] {module_name} ({version})"
    except ImportError:
        return True, f"[MISSING] {module_name} - install via pip -r requirements.txt or poetry install"


def check_dependencies() -> Tuple[List[str], List[str]]:
    missing_msgs: List[str] = []
    ok_msgs: List[str] = []
    for name in ("pandas", "numpy", "matplotlib", "requests"):
        missing, msg = try_import(name)
        if missing:
            missing_msgs.append(msg)
        else:
            ok_msgs.append(msg)
    return ok_msgs, missing_msgs


def run_analysis() -> None:
    try:
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
    except ImportError as exc:
        print(f"Cannot run analysis, missing dependency: {exc}")
        return

    print("Analyzing Matrix data...")
    data = np.random.normal(loc=0.0, scale=1.0, size=1_000)
    df = pd.DataFrame({"signal": data})
    stats: Dict[str, float] = {
        "mean": float(df["signal"].mean()),
        "std": float(df["signal"].std()),
        "min": float(df["signal"].min()),
        "max": float(df["signal"].max()),
    }
    print(f"Processing {len(df)} data points...")
    print("Stats:", stats)

    plt.figure(figsize=(6, 4))
    plt.hist(df["signal"], bins=30, color="green", alpha=0.7)
    plt.title("Matrix Signal Distribution")
    plt.xlabel("signal")
    plt.ylabel("frequency")
    output_path = "matrix_analysis.png"
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Results saved to: {output_path}")


def compare_pip_vs_poetry() -> None:
    print("Dependency management modes:")
    print("- pip:    pip install -r requirements.txt")
    print("- poetry: poetry install && poetry run python loading.py")
    print("Use one method per environment to avoid conflicts.")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    ok_msgs, missing_msgs = check_dependencies()
    print("Checking dependencies:")
    for msg in ok_msgs:
        print(msg)
    for msg in missing_msgs:
        print(msg)

    if missing_msgs:
        print("Dependencies missing. Install them with pip or poetry and re-run.")
        compare_pip_vs_poetry()
        return

    run_analysis()
    compare_pip_vs_poetry()


if __name__ == "__main__":
    main()
