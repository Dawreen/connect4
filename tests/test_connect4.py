from connect4 import __version__


def test_version():
    print("Test on version...")
    assert __version__ == '0.1.0'

print("Running test!")
test_version()
print("OK!")