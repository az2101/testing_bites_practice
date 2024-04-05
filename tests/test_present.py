
import pytest 
from lib.present import *

def test_wrap_and_then_unwrap():
    present = Present()
    present.wrap(5)
    assert present.unwrap() == 5

def test_wrap_twice_raises_exception():
    present = Present()
    present.wrap(5)
    with pytest.raises(Exception) as e:
        present.wrap(7)
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_unwrap_without_wrap_raises_exception():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

    
