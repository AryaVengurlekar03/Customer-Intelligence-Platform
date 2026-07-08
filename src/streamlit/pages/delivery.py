import streamlit as st

from utils.loader import Loader

from components.charts import (
    delivery_status_chart,
    monthly_delivery_chart,
    delivery_state_chart
)


def show_delivery():

    st.title("🚚 Delivery Analytics")

    loader = Loader()

    avg = loader.average_delivery_days().iloc[0]["avg_days"]

    st.metric(
        "Average Delivery Time",
        f"{avg} Days"
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        status_df = loader.delivery_status()

        st.plotly_chart(
            delivery_status_chart(status_df),
            use_container_width=True
        )

    with col2:

        state_df = loader.deliveries_by_state()

        st.plotly_chart(
            delivery_state_chart(state_df),
            use_container_width=True
        )

    st.divider()

    monthly_df = loader.monthly_deliveries()

    st.plotly_chart(
        monthly_delivery_chart(monthly_df),
        use_container_width=True
    )

    st.success("""
### Delivery Insights

• Most orders are delivered on time.

• Delivery volume follows overall sales trends.

• Major states account for the highest delivery volume.

• Average delivery time is calculated using actual delivery dates.
""")