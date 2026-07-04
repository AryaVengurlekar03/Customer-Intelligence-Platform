from src.etl.extract import extract_data
from src.etl.validate import validate_data
from src.etl.transform import transform_dataframe, save_interim
from src.etl.load import load_table


def run_pipeline():
    print("=" * 70)
    print("CUSTOMER INTELLIGENCE PLATFORM - ETL PIPELINE")
    print("=" * 70)

    # Step 1: Extract
    datasets = extract_data()

    # Step 2: Validate
    datasets = validate_data(datasets)

    # Step 3–5: Transform → Save → Load
    for table_name, df in datasets.items():

        transformed_df = transform_dataframe(df, table_name)

        save_interim(transformed_df, table_name)

        load_table(transformed_df, table_name)

    print("=" * 70)
    print("🎉 ETL PIPELINE COMPLETED SUCCESSFULLY!")
    print("=" * 70)


if __name__ == "__main__":
    run_pipeline()