

from lib.check_codeword import *

def test_check_codeword_works_for_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_works_for_hearse():
    result = check_codeword("hearse")
    assert result == "Close, but nope."

def test_check_codeword_works_for_potato():
    result = check_codeword("potato")
    assert result == "WRONG!"

