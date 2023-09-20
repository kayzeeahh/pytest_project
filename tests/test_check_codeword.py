from lib.check_codeword import *

def test_check_codeword_is_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."
def test_with_close_codeword():
    result = check_codeword("hqwerte")
    assert result == "Close, but nope."
def test_with_incorrect_codeword():
    result = check_codeword("baby")
    assert result == "WRONG!"