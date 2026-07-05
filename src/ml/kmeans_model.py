from pathlib import Path

import joblib
import pandas as pd
from sklearn.cluster import KMeans

from src.ml.preprocess import preprocess

OUTPUT_DIR = Path("ml_output")
MODEL_DIR = Path("models")

OUTPUT_DIR.mkdir(exist_ok=True)
MODEL_DIR.mkdir(exist_ok=True)


def train_model(k=5):

    df, scaled_data = preprocess()

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    clusters = model.fit_predict(scaled_data)

    df["cluster"] = clusters

    df.to_csv(
        OUTPUT_DIR / "customer_clusters.csv",
        index=False
    )

    joblib.dump(
        model,
        MODEL_DIR / "kmeans_model.pkl"
    )

    print("=" * 60)
    print("K-MEANS MODEL TRAINED")
    print("=" * 60)

    print(f"Clusters Created : {k}")

    print("\nCustomers per Cluster\n")

    print(df["cluster"].value_counts().sort_index())

    print("\nSaved:")

    print(OUTPUT_DIR / "customer_clusters.csv")

    print(MODEL_DIR / "kmeans_model.pkl")

    return df, model


if __name__ == "__main__":
    train_model()