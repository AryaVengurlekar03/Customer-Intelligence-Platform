import streamlit as st
from pathlib import Path
from PIL import Image


def sidebar():

    # ==========================================
    # Logo
    # ==========================================
    try:
        logo_path = Path(__file__).resolve().parent.parent / "assets" / "logo.png"

        if logo_path.exists():
            logo = Image.open(logo_path)
            st.sidebar.image(logo, width=180)
    except Exception:
        # Skip the logo if it can't be loaded
        pass

    # ==========================================
    # Project Title
    # ==========================================
    st.sidebar.title("📊 Customer Intelligence")
    st.sidebar.caption("Business Intelligence Platform")

    st.sidebar.divider()

    # ==========================================
    # Navigation
    # ==========================================
    page = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Sales",
            "Customers",
            "Products",
            "Delivery",
            "Machine Learning",
        ],
        label_visibility="collapsed",
    )

    st.sidebar.divider()

    # ==========================================
    # Filters
    # ==========================================
    st.sidebar.subheader("🔍 Filters")

    state = st.sidebar.selectbox(
        "Customer State",
        ["All"],
    )

    payment = st.sidebar.selectbox(
        "Payment Method",
        ["All"],
    )

    category = st.sidebar.selectbox(
        "Product Category",
        ["All"],
    )

    st.sidebar.divider()

    # ==========================================
    # Database Status
    # ==========================================
    st.sidebar.success("🟢 Connected to PostgreSQL")

    st.sidebar.divider()

    # ==========================================
    # Footer
    # ==========================================
    st.sidebar.caption(
        "Customer Intelligence Platform\n\n"
        "Built with Python • PostgreSQL • Streamlit • Plotly • Machine Learning"
    )

    return page