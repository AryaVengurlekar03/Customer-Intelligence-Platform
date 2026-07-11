import streamlit as st

from utils.loader import Loader

from components.charts import (
    category_revenue_chart,
    top_products_chart,
    revenue_distribution_chart
)


def show_products():

    st.title("📦 Product Analytics")

    loader = Loader()

    total = loader.total_products().iloc[0]["products"]

    st.metric(
        "Total Products",
        f"{total:,}"
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        category_df = loader.top_product_categories()

        st.plotly_chart(
            category_revenue_chart(category_df),
            use_container_width=True
        )

    with col2:

        revenue_df = loader.product_revenue_distribution()

        st.plotly_chart(
            revenue_distribution_chart(revenue_df),
            use_container_width=True
        )

    st.divider()

    product_df = loader.top_products()

    st.plotly_chart(
        top_products_chart(product_df),
        use_container_width=True
    )

    st.success("""
### Product Insights

• Electronics and home products generate the highest revenue.

• A small number of products contribute significantly to total sales.

• Product category distribution helps identify profitable segments.
""")