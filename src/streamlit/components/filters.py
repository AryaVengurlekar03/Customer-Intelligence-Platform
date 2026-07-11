import streamlit as st


def show_filters():

    st.sidebar.header("🔍 Filters")

    state = st.sidebar.selectbox(
        "Customer State",
        ["All"]
    )

    payment = st.sidebar.selectbox(
        "Payment Method",
        ["All"]
    )

    category = st.sidebar.selectbox(
        "Product Category",
        ["All"]
    )

    return state, payment, category