# 0.7.0

- add `pdx.Database` #22
- fix pyarrow bug #19

# 0.5.0

- drop `prql`; i never use it

# 0.4.0

- remove `get_params` (as that's really for external queries that need to work with Jinja)
- query functions can also take a filename (instead of just a query string)
- change default table name to `_df`
- handle CTEs correctly for `df.sql()`: avoid prepending `from {table_name}` to the query string

# 0.3.0

- add `pdx.__version__`
- use "FROM-first" syntax in DuckDB: https://duckdb.org/2022/11/14/announcing-duckdb-060.html
