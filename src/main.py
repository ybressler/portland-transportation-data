# -*- coding: utf-8 -*-
import duckdb


def load_extension(conn: duckdb.DuckDBPyConnection):
    """Install and load extensions"""
    conn.install_extension("spatial")
    conn.load_extension("spatial")


def load_data(conn: duckdb.DuckDBPyConnection, replace: bool = False):
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
        conn.sql(f"{create_command} {table_name} AS SELECT  * FROM read_csv_auto('{file_path}')")



if __name__ == '__main__':

    conn: duckdb.DuckDBPyConnection = duckdb.connect("my_db.db")

    # Load extensions
    load_extension(conn)
    load_data(conn)

    conn.sql("SHOW ALL TABLES;").show()
    df = conn.sql('SELECT * FROM traffic_signals').df()  # Converts to a pandas df
    print(df.head())
