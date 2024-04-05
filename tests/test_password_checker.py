
import pytest
from lib.password_checker import *

def test_suitable_password():
    passwordchecker = PasswordChecker()
    assert passwordchecker.check('eightletters') == True

def test_short_password():
    passwordchecker = PasswordChecker()
    with pytest.raises(Exception) as e:
        passwordchecker.check('hello')
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."


    