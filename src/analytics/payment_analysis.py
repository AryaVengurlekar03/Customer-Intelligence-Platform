from src.analytics.database_reader import execute_query


def main():

    print("=" * 70)
    print("PAYMENT ANALYSIS REPORT")
    print("=" * 70)

    # Payment Method Summary
    query_payment_method = """
    SELECT
        payment_type,
        COUNT(*) AS total_transactions,
        ROUND(SUM(payment_value),2) AS total_revenue,
        ROUND(AVG(payment_value),2) AS average_payment
    FROM payments
    GROUP BY payment_type
    ORDER BY total_revenue DESC;
    """

    payment_method_df = execute_query(query_payment_method)

    print("\nPayment Method Summary\n")
    print(payment_method_df)

    payment_method_df.to_csv(
        "reports/payment_method_summary.csv",
        index=False
    )

    # Installment Analysis
    query_installments = """
    SELECT
        payment_installments,
        COUNT(*) AS total_transactions,
        ROUND(SUM(payment_value),2) AS total_revenue,
        ROUND(AVG(payment_value),2) AS average_payment
    FROM payments
    GROUP BY payment_installments
    ORDER BY payment_installments;
    """

    installment_df = execute_query(query_installments)

    print("\nInstallment Analysis\n")
    print(installment_df)

    installment_df.to_csv(
        "reports/payment_installments.csv",
        index=False
    )

    # Highest Value Payments
    query_top_payments = """
    SELECT
        order_id,
        payment_type,
        payment_installments,
        ROUND(payment_value,2) AS payment_value
    FROM payments
    ORDER BY payment_value DESC
    LIMIT 20;
    """

    top_payment_df = execute_query(query_top_payments)

    print("\nTop 20 Highest Payments\n")
    print(top_payment_df)

    top_payment_df.to_csv(
        "reports/top_payments.csv",
        index=False
    )

    print("\n" + "=" * 70)
    print("PAYMENT ANALYSIS COMPLETED")
    print("=" * 70)
    print("Generated Reports:")
    print("✓ payment_method_summary.csv")
    print("✓ payment_installments.csv")
    print("✓ top_payments.csv")


if __name__ == "__main__":
    main()