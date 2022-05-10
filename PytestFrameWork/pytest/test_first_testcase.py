import pytest




def setup_module(module):
    print("creating DB connection")


def teardown_module(module):
    print("closing DB connection")

def setup_function(function):
    print("launchin browser")


def teardown_function(function):
    print("quit the browser")



def test_dologin():
    print("Executing login test")

def test_user_reg():
    print("Executing user reg test")

