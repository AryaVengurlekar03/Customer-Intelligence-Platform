import streamlit as st


def show_kpis(revenue, orders, customers, sellers):

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "💰 Revenue",
        f"${revenue:,.0f}"
    )

    c2.metric(
        "📦 Orders",
        f"{orders:,}"
    )

    c3.metric(
        "👥 Customers",
        f"{customers:,}"
    )

    c4.metric(
        "🏪 Sellers",
        f"{sellers:,}"
    )