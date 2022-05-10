

import pytest

def test_validate():
    expected_tiltel = "google.com"
    unexcepted_title = "yahoo.com"
    title = "this is gmail website"

    assert expected_tiltel == unexcepted_title, "doesnot match"
    assert "gmaijl" in title, "gmail doesnt exist"
    assert False, "forecefully failed"


#if we want to execute multiple assert, so we go for pytest test_adsbalsd.py -s -v --soft-asserts

