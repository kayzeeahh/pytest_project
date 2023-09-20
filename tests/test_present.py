import pytest 
from lib.present import *

def test_for_wrap_and_unwrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33
    
# if we unwrap before wrapping

def  test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as err:
        present.unwrap()
    message = str(err.value)
    assert message == "No contents have been wrapped."
    
# if we try to wrap twice

def test_already_wrapped_present():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as err:
        present.wrap(66)
    message = str(err.value)
    assert message == "A contents has already been wrapped."