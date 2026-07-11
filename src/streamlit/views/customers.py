import streamlit as st

from utils.loader import Loader

from components.charts import (
    customer_distribution_chart,
    revenue_state_chart,
    top_customers_chart
)


def show_customers():

    st.title("👥 Customer Analytics")

    loader = Loader()

    total = loader.unique_customers().iloc[0]["customers"]

    st.metric(
        "Unique Customers",
        f"{total:,}"
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        customer_df = loader.customer_distribution()

        st.plotly_chart(
            customer_distribution_chart(customer_df),
            use_container_width=True
        )

    with col2:

        revenue_df = loader.revenue_state()

        st.plotly_chart(
            revenue_state_chart(revenue_df),
            use_container_width=True
        )

    st.divider()

    top_df = loader.top_customers()

    st.plotly_chart(
        top_customers_chart(top_df),
        use_container_width=True
    )

    st.success("""
### Insights

• Customer base spans all Brazilian states.

• A few states contribute the majority of revenue.

• Top customers account for a significant share of sales.
""")