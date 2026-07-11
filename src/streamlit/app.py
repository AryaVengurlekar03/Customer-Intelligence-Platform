import streamlit as st

from utils.theme import load_theme
from components.sidebar import sidebar

from views.dashboard import show_dashboard
from views.sales import show_sales
from views.customers import show_customers
from views.products import show_products
from views.delivery import show_delivery
from views.ml_dashboard import show_ml_dashboard


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

   