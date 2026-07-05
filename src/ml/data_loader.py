from pathlib import Path

import pandas as pd


REPORTS_DIR = Path("reports")


def load_customer_segments():

    file = REPORTS_DIR / "customer_segments.csv"

    if not file.exists():
        raise FileNotFoundError(
            "Run customer_segmentation.py first."
        )

    return pd.read_csv(file)


if __name__ == "__main__":

    df = load_customer_segments()

    print(df.head())

    print()

    print(df.info())