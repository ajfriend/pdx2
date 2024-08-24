# PDX: Helper functions to run SQL on Pandas DataFrames

```shell
pip install git+https://github.com/ajfriend/pdx
```

Small ergonomic improvements to make it easy to run [DuckDB](https://duckdb.org/) queries on Pandas dataframes.

- `pdx` monkey-patches Pandas to provide a `df.sql(...)` method.
- since `pdx` uses DuckDB, you can leverage their convienient SQL dialect:
  - https://duckdb.org/2022/05/04/friendlier-sql.html
  - https://duckdbsnippets.com/


Query a dataframe with `df.sql(...)`.
Omit the `FROM` clause because it is included implicitly:

```python
import pdx
iris = pdx.data.get_iris()

iris.sql("""
select
    species,
    count(*)
        as num,
group by
    1
""")
```

You can use short SQL (sub-)expressions because `FROM` and `SELECT *` are implied whenever they're omitted:

```python
iris.sql('where petal_length > 4.5')
```

```python
iris.sql('limit 10')
```

```python
iris.sql('order by petal_length')
```

```python
iris.sql('')  # returns the dataframe unmodified. I.e., 'select * from iris'
```

For more, check out the [example notebook folder](notebooks).

# Other affordances

- `df.aslist()`
- `df.asdict()`
- `df.asitem()`
- `df.cols2dict()`
- save/load helpers for DuckDB database files

# Reference

- [Apache Arrow and the "10 Things I Hate About pandas"](https://wesmckinney.com/blog/apache-arrow-pandas-internals/)

## For bleeding edge DuckDB

```
git clone https://github.com/duckdb/duckdb.git
cd duckdb
../env/bin/pip install -e tools/pythonpkg --verbose
```
