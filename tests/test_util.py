from commando import util


def test_str_to_list():
    res = util.str_to_list("mkdir test")
    assert res == ["mkdir", "test"]


def test_str_to_list_multiple_space():
    res = util.str_to_list("mkdir   test")
    assert res == ["mkdir", "test"]
