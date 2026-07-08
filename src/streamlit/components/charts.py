import plotly.express as px


def revenue_chart(df):

    fig = px.line(
        df,
        x="month",
        y="revenue",
        markers=True,
        title="Monthly Revenue"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    return fig


def state_chart(df):

    fig = px.bar(
        df,
        x="customer_state",
        y="revenue",
        title="Revenue by State"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    return fig


def payment_chart(df):

    fig = px.pie(
        df,
        names="payment_type",
        values="total",
        title="Payment Methods"
    )

    fig.update_layout(height=450)

    return fig
def category_chart(df):

    fig = px.bar(
        df,
        x="revenue",
        y="category",
        orientation="h",
        title="Top Product Categories"
    )

    fig.update_layout(height=450)

    return fig
def status_chart(df):

    fig = px.pie(
        df,
        names="order_status",
        values="total",
        hole=0.5,
        title="Order Status"
    )

    fig.update_layout(height=450)

    return fig
def orders_chart(df):

    fig = px.bar(
        df,
        x="month",
        y="total_orders",
        title="Monthly Orders"
    )

    fig.update_layout(height=450)

    return fig
def sellers_chart(df):

    fig = px.bar(
        df,
        x="revenue",
        y="seller_id",
        orientation="h",
        title="Top Sellers"
    )

    fig.update_layout(height=450)

    return fig
def customer_distribution_chart(df):

    fig = px.bar(
        df,
        x="customer_state",
        y="customers",
        title="Customer Distribution by State"
    )

    fig.update_layout(
        height=450,
        template="plotly_white"
    )

    return fig
def revenue_state_chart(df):

    fig = px.bar(
        df,
        x="customer_state",
        y="revenue",
        title="Revenue by State"
    )

    fig.update_layout(
        height=450,
        template="plotly_white"
    )

    return fig
def top_customers_chart(df):

    fig = px.bar(
        df,
        x="revenue",
        y="customer_unique_id",
        orientation="h",
        title="Top Customers"
    )

    fig.update_layout(
        height=450,
        template="plotly_white"
    )

    return fig
def category_revenue_chart(df):

    fig = px.bar(
        df,
        x="revenue",
        y="category",
        orientation="h",
        title="Top Product Categories"
    )

    fig.update_layout(
        height=450,
        template="plotly_white"
    )

    return fig
def top_products_chart(df):

    fig = px.bar(
        df,
        x="revenue",
        y="product_id",
        orientation="h",
        title="Highest Revenue Products"
    )

    fig.update_layout(
        height=450,
        template="plotly_white"
    )

    return fig
def revenue_distribution_chart(df):

    fig = px.pie(
        df,
        names="category",
        values="revenue",
        title="Revenue Distribution by Category"
    )

    fig.update_layout(
        height=450
    )

    return fig
def delivery_status_chart(df):

    fig = px.pie(
        df,
        names="delivery_status",
        values="total",
        hole=0.5,
        title="Delivery Performance"
    )

    fig.update_layout(
        height=450
    )

    return fig
def monthly_delivery_chart(df):

    fig = px.line(
        df,
        x="month",
        y="deliveries",
        markers=True,
        title="Monthly Deliveries"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    return fig
def delivery_state_chart(df):

    fig = px.bar(
        df,
        x="customer_state",
        y="deliveries",
        title="Deliveries by State"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    return fig
def cluster_chart(df):

    fig = px.bar(
        df,
        x="cluster",
        y="customers",
        color="cluster",
        title="Customer Cluster Distribution"
    )

    fig.update_layout(
        template="plotly_white",
        height=450,
        showlegend=False
    )

    return fig
import plotly.express as px


def cluster_distribution_chart(df):

    fig = px.histogram(

        df,

        x="cluster",

        color="cluster",

        title="Customer Cluster Distribution"

    )

    fig.update_layout(

        template="plotly_white",

        height=500,

        showlegend=False

    )

    return fig