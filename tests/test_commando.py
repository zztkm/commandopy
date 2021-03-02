from commando import __version__
from commando import commando


def test_version():
    assert __version__ == '1.0.0'


def test_add():
    commando.add("mkdir test")
    cmd_list = commando.list()
    assert cmd_list == ["mkdir test"]


def test_add_multiple():
    commando.add("touch test\test.py")
    cmd_list = commando.list()
    print(cmd_list)
    assert cmd_list == ["mkdir test", "touch test\test.py"]
