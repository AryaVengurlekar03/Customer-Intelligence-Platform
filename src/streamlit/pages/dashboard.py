import streamlit as st

from utils.loader import Loader

from components.kpi_cards import show_kpis

from components.charts import (
    revenue_chart,
    state_chart,
    payment_chart,
    category_chart,
    status_chart
)


def show_dashboard():

    st.title("📊 Executive Dashboard")
    st.caption("Real-time Business Intelligence Dashboard")

    loader = Loader()

    # ==========================================================
    # KPI CARDS
    # ==========================================================

    revenue = loader.total_revenue().iloc[0]["revenue"]
    orders = loader.total_orders().iloc[0]["orders"]
    customers = loader.total_customers().iloc[0]["customers"]
    sellers = loader.total_sellers().iloc[0]["sellers"]

    show_kpis(
        revenue,
        orders,
        customers,
        sellers
    )

    st.divider()

    # ==========================================================
    # MONTHLY REVENUE
    # ==========================================================

    revenue_df = loader.monthly_revenue()

    st.plotly_chart(
        revenue_chart(revenue_df),
        use_container_width=True
    )

    st.divider()

    # ==========================================================
    # STATE + PAYMENT
    # ==========================================================

    col1, col2 = st.columns(2)

    with col1:

        state_df = loader.revenue_by_state()

        st.plotly_chart(
            state_chart(state_df),
            use_container_width=True
        )

    with col2:

        payment_df = loader.payment_methods()

        st.plotly_chart(
            payment_chart(payment_df),
            use_container_width=True
        )

    st.divider()

    # ==========================================================
    # CATEGORY + STATUS
    # ==========================================================

    col3, col4 = st.columns(2)

    with col3:

        category_df = loader.top_categories()

        st.plotly_chart(
            category_chart(category_df),
            use_container_width=True
        )

    with col4:

        status_df = loader.order_status()

        st.plotly_chart(
            status_chart(status_df),
            use_container_width=True
        )

    st.divider()

    # ==========================================================
    # BUSINESS INSIGHTS
    # ==========================================================

    st.subheader("📌 Business Insights")

    c1, c2 = st.columns(2)

    with c1:

        st.success(f"""
### Highlights

- 💰 Total Revenue : **${revenue:,.2f}**

- 📦 Orders Processed : **{orders:,}**

- 👥 Unique Customers : **{customers:,}**

- 🏪 Active Sellers : **{sellers:,}**
""")

    with c2:

        st.info("""
### Executive Summary

✔ Revenue is healthy across the platform.

✔ Customer acquisition is strong.

✔ Multiple payment methods are actively used.

✔ Product sales are concentrated in a few top categories.

✔ Dashboard data is loaded directly from PostgreSQL.
""")