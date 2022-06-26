from commando import __version__, commando


def test_version():
    assert __version__ == "1.0.2"


def test_add():
    commando.add("mkdir test")
    cmd_list = commando.list()
    assert cmd_list == ["mkdir test"]


def test_add_multiple():
    commando.add("cd test")
    cmd_list = commando.list()
    assert cmd_list == ["mkdir test", "cd test"]
