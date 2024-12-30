import pdx2
from pytest import approx


def test_from_first_sql():
    iris = pdx2.data.get_iris()

    foo = lambda s: iris.sql(s).asitem()

    assert (
        foo('select avg(sepal_length)')
        ==
        approx(5.843333333333335)
    )

    assert (
        foo('select avg(sepal_length) where sepal_length < 6.0')
        ==
        approx(5.224096385542169)
    )

    assert (
        foo('select avg(sepal_length) where sepal_length > 6.0')
        ==
        approx(6.670491803278686)
    )


def test_default_table_name_and_CTE():
    iris = pdx2.data.get_iris()

    out = iris.sql("""
    with _ as (select 1)

    select
        count(*)
    from
        _df
    """).asitem()

    assert out == 150
