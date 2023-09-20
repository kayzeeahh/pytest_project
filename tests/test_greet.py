from lib.greet import *

def test_greet_keziah_with_name():
    result = greet("Keziah")
    assert result == "Hello, Keziah!"