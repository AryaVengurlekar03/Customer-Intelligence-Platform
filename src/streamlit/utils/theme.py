import streamlit as st


def load_theme():

    st.set_page_config(
        page_title="Customer Intelligence Platform",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.markdown("""
    <style>

    .main{
        background:#F5F7FA;
    }

    div[data-testid="metric-container"]{

        background:white;

        border-radius:15px;

        padding:20px;

        box-shadow:0 2px 8px rgba(0,0,0,.1);

    }

    h1{
        color:#1F4E79;
    }

    </style>
    """, unsafe_allow_html=True)
    