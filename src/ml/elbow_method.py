from pathlib import Path

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

from src.ml.preprocess import preprocess

OUTPUT_DIR = Path("ml_output")
OUTPUT_DIR.mkdir(exist_ok=True)


def find_optimal_clusters():

    _, scaled_data = preprocess()

    wcss = []

    for k in range(1, 11):

        model = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        model.fit(scaled_data)

        wcss.append(model.inertia_)

    plt.figure(figsize=(8, 5))

    plt.plot(
        range(1, 11),
        wcss,
        marker="o"
    )

    plt.title("Elbow Method")
    plt.xlabel("Number of Clusters")
    plt.ylabel("WCSS")
    plt.grid(True)

    output = OUTPUT_DIR / "elbow_method.png"

    plt.savefig(output, dpi=300)

    plt.close()

    print("=" * 60)
    print("ELBOW METHOD COMPLETED")
    print("=" * 60)
    print(f"Plot saved at: {output}")


if __name__ == "__main__":
    find_optimal_clusters()