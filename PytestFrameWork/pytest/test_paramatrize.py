
import pytest


def get_data():

    return [


        ("clintonnayagam@gmail.com","Clinton@97"),
        ("clintonvinoth97@gmail.com", "Vinoth@97"),
        ("clintonvinoth87@gmail.com", "Vimal@97")
    ]

@pytest.mark.parametrize("username,password",get_data())
def test_dologin(username,password):
    print(username,"---",password)