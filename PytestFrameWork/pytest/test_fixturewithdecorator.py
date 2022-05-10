import pytest





@pytest.fixture(scope='module')
def setup():
    print("Creating DB connection")


    yield ##yuield will act as teardown
    print("closing DB connection")
@pytest.fixture(scope='function')
def before():
    print("launching browser")

    yield
    print("closing browser")

#def test_dologin(setup,before):
#    print("Executing login test")

#def test_user_reg(setup,before):
#    print("Executing user reg test")


#another way of line no 21-25

@pytest.mark.usefixtures("setup","before")
def test_dologin():
    print("Executing login test")

@pytest.mark.usefixtures("setup","before")
def test_user_reg(setup,before):
    print("Executing user reg test")
