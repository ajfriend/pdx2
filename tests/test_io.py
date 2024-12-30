import pdx2
import os

def test_one():
    df = pdx2.data.get_iris()

    filename = 'test.duckdb'

    pdx2.save(filename, table_name=df)
    out = pdx2.load(filename)

    try:
        os.remove(filename)
    except OSError:
        pass

    assert 'table_name' in out
    assert 'wrong_name' not in out

    out_df = out['table_name']

    assert (df == out_df).all().all()
