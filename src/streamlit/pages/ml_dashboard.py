import streamlit as st

from PIL import Image

from utils.loader import Loader

from components.charts import (
    cluster_distribution_chart
)


def show_ml_dashboard():

    st.title("🤖 Machine Learning Dashboard")

    loader = Loader()

    clusters = loader.customer_clusters()

    summary = loader.cluster_summary()

    report = loader.cluster_report()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Customers",
        f"{len(clusters):,}"
    )

    col2.metric(
        "Clusters",
        clusters.cluster.nunique()
    )

    col3.metric(
        "Model",
        "K-Means"
    )

    st.divider()

    st.plotly_chart(

        cluster_distribution_chart(clusters),

        use_container_width=True

    )

    st.divider()

    st.subheader("Cluster Summary")

    st.dataframe(

        summary,

        use_container_width=True

    )

    st.divider()

    st.subheader("PCA Visualization")

    st.image(

        Image.open(
            "ml_output/customer_clusters_pca.png"
        ),

        use_container_width=True

    )

    st.divider()

    st.subheader("Elbow Method")

    st.image(

        Image.open(
            "ml_output/elbow_method.png"
        ),

        use_container_width=True

    )

    st.divider()

    st.subheader("Cluster Report")

    st.code(report)

    st.success("""

### Business Recommendations

🏆 Champions → Reward and retain

💙 Loyal Customers → Upsell

🟢 Potential Loyalists → Convert into loyal buyers

🟠 Budget Buyers → Offer discounts

🔴 At Risk → Win-back campaigns

""")