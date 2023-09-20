import pytest
from lib.password_checker import *

# test to see if password is 8+ characters

def test_to_see_if_valid():
    password_checker = PasswordChecker()
    password_checker.check("Password1")
    assert password_checker 
    
def test_to_see_if_invalid():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as err:
        password_checker.check("weak")
    message = str(err.value)
    assert message == "Invalid password, must be 8+ characters."