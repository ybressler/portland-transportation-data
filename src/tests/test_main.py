# -*- coding: utf-8 -*-
"""
Unittests for main executables
"""
import pytest

from src.main import load_extension, load_data


def test_load_extensions(db_conn):
    """Ensures extensions can be loaded"""
    load_extension(db_conn)


@pytest.mark.parametrize('replace', [True, False])
def test_load_data(db_conn, replace: bool):
    """Ensures data can be loaded (without extensions)"""

    # Load data without extensions
    load_data(conn=db_conn, replace=replace)
