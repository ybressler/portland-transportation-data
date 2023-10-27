# -*- coding: utf-8 -*-
import duckdb

con: duckdb.DuckDBPyConnection = duckdb.connect("my_db.db")


def load_extension(con: duckdb.DuckDBPyConnection):
    """Install and load extensions"""
    con.install_extension("spatial")
    con.load_extension("spatial")


def load_data(con: duckdb.DuckDBPyConnection, replace: bool = False):
    """
    Load data from compressed csv | geojson format.

    Args:
        con: Database connection
        replace: Replace tables if they exist? (Default is no, makes things faster.)
    """
    # Load data
    load_tables = [
        ("corners", "Corners_Improved.csv.gz"),
        ("curbs", "Curbs.csv.gz"),
        ("signs", "Signs.csv.gz"),
        ("traffic_signals", "Traffic_Signals.csv.gz"),
    ]

    if replace:
        create_command = "CREATE OR REPLACE TABLE"
    else:
        create_command = "CREATE TABLE IF NOT EXISTS"

    for table_name, file_name in load_tables:
        file_path = f"data/{file_name}"
        con.sql(f"{create_command} {table_name} AS SELECT  * FROM read_csv_auto('{file_path}')")



if __name__ == '__main__':

    # Load extensions
    load_extension(con)
    load_data(con)

    con.sql("SHOW ALL TABLES;").show()
    df = con.sql('SELECT * FROM traffic_signals').df()  # Converts to a pandas df
    print(df.head())
