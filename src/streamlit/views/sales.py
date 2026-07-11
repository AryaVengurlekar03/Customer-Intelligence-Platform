import streamlit as st

from utils.loader import Loader
from components.charts import (
    orders_chart,
    sellers_chart
)


def show_sales():

    st.title("💰 Sales Analytics")

    loader = Loader()

    avg = loader.average_order_value().iloc[0]["avg_order_value"]

    st.metric(
        "Average Order Value",
        f"${avg:,.2f}"
    )

    st.divider()

    orders = loader.monthly_orders()

    st.plotly_chart(
        orders_chart(orders),
        use_container_width=True
    )

    st.divider()

    sellers = loader.top_sellers()

    st.plotly_chart(
        sellers_chart(sellers),
        use_container_width=True
    )