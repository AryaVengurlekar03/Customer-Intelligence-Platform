def validate_data(datasets):
    """
    Validate all extracted datasets.
    """

    print("\n" + "=" * 60)
    print("VALIDATING DATASETS")
    print("=" * 60)

    for table_name, df in datasets.items():

        if df.empty:
            raise ValueError(f"{table_name} dataset is empty!")

        print(
            f"✅ {table_name:<22}"
            f" Rows: {len(df):>8} | Columns: {len(df.columns):>2}"
        )

    print("=" * 60)
    print("All datasets validated successfully.\n")

    return datasets