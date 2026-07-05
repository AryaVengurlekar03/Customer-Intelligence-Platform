from pathlib import Path

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

from src.ml.preprocess import preprocess
from src.ml.kmeans_model import train_model

OUTPUT_DIR = Path("ml_output")
OUTPUT_DIR.mkdir(exist_ok=True)


def visualize_clusters():

    df, model = train_model()

    _, scaled_data = preprocess()

    pca = PCA(n_components=2)

    components = pca.fit_transform(scaled_data)

    plt.figure(figsize=(10, 6))

    plt.scatter(
        components[:, 0],
        components[:, 1],
        c=df["cluster"],
        cmap="viridis",
        s=20
    )

    plt.title("Customer Clusters (PCA)")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")

    plt.colorbar(label="Cluster")

    output = OUTPUT_DIR / "customer_clusters_pca.png"

    plt.savefig(output, dpi=300)

    plt.close()

    print("=" * 60)
    print("PCA VISUALIZATION GENERATED")
    print("=" * 60)
    print(f"Saved: {output}")


if __name__ == "__main__":
    visualize_clusters()    