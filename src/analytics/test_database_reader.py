from src.analytics.database_reader import read_table


def main():

    customers = read_table("customers")

    print("=" * 50)
    print("DATABASE CONNECTION SUCCESSFUL")
    print("=" * 50)

    print(customers.head())

    print()

    print("Rows :", len(customers))
    print("Columns :", len(customers.columns))


if __name__ == "__main__":
    main()