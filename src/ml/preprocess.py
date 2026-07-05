from pathlib import Path

from sklearn.preprocessing import StandardScaler

from src.ml.data_loader import load_customer_segments


OUTPUT_DIR = Path("ml_output")
OUTPUT_DIR.mkdir(exist_ok=True)


def preprocess():

    df = load_customer_segments()

    features = df[
        [
            "recency",
            "frequency",
            "monetary"
        ]
    ]

    scaler = StandardScaler()

    scaled = scaler.fit_transform(features)

    return df, scaled


if __name__ == "__main__":

    df, scaled = preprocess()

    print(df.head())

    print()

    print(scaled[:5])