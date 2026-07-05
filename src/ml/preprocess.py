from pathlib import Path

from sklearn.preprocessing import StandardScaler

from src.ml.data_loader import load_customer_data

OUTPUT_DIR = Path("ml_output")
OUTPUT_DIR.mkdir(exist_ok=True)


def preprocess():

    df = load_customer_data()

    # -----------------------
    # Recency
    # -----------------------

    reference_date = df["last_purchase"].max()

    df["recency"] = (
        reference_date - df["last_purchase"]
    ).dt.days

    # -----------------------
    # Features
    # -----------------------

    features = df[
        [
            "recency",
            "frequency",
            "monetary"
        ]
    ]

    scaler = StandardScaler()

    scaled_features = scaler.fit_transform(features)

    return df, scaled_features


if __name__ == "__main__":

    df, scaled = preprocess()

    print(df.head())

    print()

    print(scaled[:5])