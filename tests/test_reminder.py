
import pytest
from lib.reminder import *

def test_reminder():
    reminder = Reminder("Andrew")
    with pytest.raises(Exception) as err:
        reminder.remind()
    error_mesage = str(err.value)
    assert error_mesage == "No reminder set!"

