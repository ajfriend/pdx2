import duckdb
import pyarrow as pa

from ._util import _get_if_file


def sql(s, **dfs):
    config = {'enable_external_access': False}
    con = duckdb.connect(database=':memory:', config=config)

    for tbl_name, df in dfs.items():
        df = pa.Table.from_pandas(df)
        con.register(tbl_name, df)

    s = _get_if_file(s)
    out = con.execute(s).df()

    return out


class Database:
    def __init__(self, **dfs):
        con = duckdb.connect(
            database = ':memory:',
            config = {'enable_external_access': False},
        )

        for tbl_name, df in dfs.items():
            df = pa.Table.from_pandas(df)
            con.register(tbl_name, df)

        self._con = con

    def __repr__(self):
        tables = yield_table_lines(self)

        s = 'pdx.Database:\n'
        for table in tables:
            s += f'    {table}'

        return s

    def sql(self, s):
        s = _get_if_file(s)
        out = self._con.execute(s).df()
        return out


def yield_table_lines(db):
    df = db.sql('show all tables')

    for _, tbl in df.iterrows():
        name = tbl['name']
        columns = list(tbl['column_names'])
        n = db.sql(f'select count() from {name}').asitem()

        yield f'{name}: {n} x {columns}'


# todo: can we do some fancier thing to specify the dicts?
# https://docs.python.org/3/library/string.html#string.Formatter.vformat
# s = """
# select
#       iris.*
#     , df2.avg_petal_width
#         as species_avg_petal_width
# from
#     {iris}
# left join
#     {df2}
# on
#     iris.species = df2.species
# """
