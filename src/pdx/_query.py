import duckdb

from ._util import _get_if_file


def sql(s, **dfs):
    config = {'enable_external_access': False}
    con = duckdb.connect(database=':memory:', config=config)

    for tbl_name, df in dfs.items():
        con.register(tbl_name, df)

    s = _get_if_file(s)
    out = con.execute(s).df()

    return out


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
