from solution import compute_obsolete


def test_compute_obsolete_returns_true():
    """
    tests that compute obsolete function returns TRUE 
    when a date less than 2021-01-01 is passed
    """
    expired = compute_obsolete('2020-11-09')
    assert expired == 'TRUE'


def test_compute_obsolete_returns_false():
    """
    tests that compute obsolete function returns FALSE 
    when a date greater than 2021-01-01 is passed
    """
    expired = compute_obsolete('2021-11-09')
    assert expired == 'FALSE'
