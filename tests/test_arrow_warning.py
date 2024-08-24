import duckdb
import pandas as pd
import pyarrow as pa

import pytest

# https://github.com/duckdb/duckdb/issues/9182

def foo(df):
    con = duckdb.connect(
        database = ':memory:',
        config = {'enable_external_access': False}
    )
    con.register('df', df)

    s = 'select * from df'
    out = con.execute(s).df()

    return out

col1 = pd.Series(['a', 'b', 'c'], dtype='string[pyarrow]')
pd_df = pd.DataFrame({'col1': col1})


def test_for_warning():
    with pytest.warns(FutureWarning):
        foo(pd_df)


def test_no_warning():
    pa_df = pa.Table.from_pandas(pd_df)

    foo(pa_df)

def test_with_pdx():
    import pdx
    pd_df.sql()  # should run without warning
