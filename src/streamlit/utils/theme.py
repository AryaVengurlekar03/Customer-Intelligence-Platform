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
        background:#F8FAFC;
    }

    section[data-testid="stSidebar"]{
        background:#1E293B;
    }

    section[data-testid="stSidebar"] *{
        color:white;
    }

    div[data-testid="metric-container"]{

        background:white;

        border-radius:15px;

        padding:20px;

        box-shadow:0px 4px 10px rgba(0,0,0,.15);

        border-left:6px solid #2563EB;

    }

    h1,h2,h3{
        color:#0F172A;
        font-weight:700;
    }
/* Hide Streamlit Main Menu */
#MainMenu {
    visibility: hidden;
}

/* Hide Streamlit Footer */
footer {
    visibility: hidden;
}

/* Hide Header */
header {
    visibility: hidden;
}
    </style>
 """, unsafe_allow_html=True)