import streamlit as st

from utils.theme import load_theme
from components.sidebar import sidebar

from pages.dashboard import show_dashboard
from pages.sales import show_sales
from pages.customers import show_customers
from pages.products import show_products
from pages.delivery import show_delivery
from pages.ml_dashboard import show_ml_dashboard


# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------
load_theme()

# -------------------------------------------------------
# Sidebar Navigation
# -------------------------------------------------------
page = sidebar()

# -------------------------------------------------------
# Route to Selected Page
# -------------------------------------------------------
if page == "Dashboard":
    show_dashboard()

elif page == "Sales":
    show_sales()

elif page == "Customers":
    show_customers()

elif page == "Products":
    show_products()

elif page == "Delivery":
    show_delivery()

elif page == "Machine Learning":
    show_ml_dashboard()