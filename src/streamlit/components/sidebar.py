from streamlit_option_menu import option_menu
import streamlit as st


def sidebar():

    with st.sidebar:

        selected = option_menu(

            "Navigation",

            [

                "Dashboard",

                "Sales",

                "Customers",

                "Products",

                "Delivery",

                "Machine Learning"

            ],

            icons=[

                "speedometer2",

                "graph-up",

                "people",

                "box",

                "truck",

                "cpu"

            ],

            default_index=0

        )

    return selected