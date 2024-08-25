import pdx
import pytest


def test_db():
    iris = pdx.data.get_iris()
    db = pdx.Database(iris=iris)

    out = db.sql("""
    select
          avg(sepal_length)  as sl
        , avg(sepal_width)   as sw
        , avg(petal_length)  as pl
        , avg(petal_width)   as pw
    from
        iris
    """).asdict()

    ex = {
        'sl': 5.843,
        'sw': 3.057,
        'pl': 3.758,
        'pw': 1.199,
    }

    assert out == pytest.approx(ex, rel=1e-3)


def test_repr():
    from textwrap import dedent
    iris = pdx.data.get_iris()
    db = pdx.Database(iris=iris)

    ex = """
    pdx.Database:
        iris: 150 x ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    """
    ex = dedent(ex)
    ex = ex.strip()

    assert repr(db) == ex
