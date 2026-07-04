from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

INTERIM = BASE_DIR / "data" / "interim"

INTERIM.mkdir(exist_ok=True)


def save_interim(df, table):

    file = INTERIM / f"{table}.csv"

    df.to_csv(file, index=False)

    return file