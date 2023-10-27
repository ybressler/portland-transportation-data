# -*- coding: utf-8 -*-
import duckdb

con: duckdb.DuckDBPyConnection = duckdb.connect()

def load_extension(con: duckdb.DuckDBPyConnection):
    """Install and load extensi9ons"""
    con.install_extension("spatial")
    con.load_extension("spatial")


def load_data(con: duckdb.DuckDBPyConnection):
    """Load data from tables"""
    # Load data
    duckdb.sql("CREATE TABLE traffic_signals_csv AS SELECT  * FROM read_csv_auto('data/Traffic_Signals.csv')")
    duckdb.sql("CREATE TABLE traffic_signals_json AS SELECT  * FROM read_json_auto('data/Traffic_Signals.geojson')")


if __name__ == '__main__':

    # Load extensions
    load_extension(con)
    load_data(con)

    df = con.sql('SELECT * FROM traffic_signals').df()  # Converts to a pandas df
    print(df.head())
