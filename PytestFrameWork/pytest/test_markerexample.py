import pytest


@pytest.mark.functional
def test_login():
    print("call login")


@pytest.mark.regression
def test_user_ref():
    print("call user ref")


@pytest.mark.functional
def test_compose_email():
    print("compose email")


@pytest.mark.skip
def test_dukaan():
    print("dukaan")
