# -*- coding: utf-8 -*-
"""Common fixtures"""
import pytest

import duckdb


@pytest.fixture(autouse=True)
def db_conn() -> duckdb.DuckDBPyConnection:
    """
    Returns an in-memory duck db connection.

    NOTE: this connection is reused throughout unittests. If you need
        an empty db connection, then create a new fixture with desired behavior.
    """
    return duckdb.connect(database=":memory:")
