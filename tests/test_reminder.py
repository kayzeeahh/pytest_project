import pytest 
from lib.reminder import *

def test_reminds_the_users_to_do_a_task():
    reminder = Reminder("Kay")
    reminder.reminder_me_to("Walk the dog")
    result = reminder.remind()
    assert result == "Walk the dog, Kay!"
    
def test_reminds_kez_to_study():
    reminder = Reminder("Kez")
    reminder.reminder_me_to("Do some coding")
    result = reminder.remind()
    assert result == "Do some coding, Kez!"
    
def test_raises_an_error_when_no_task_is_set():
    reminder = Reminder("Kez")
    with pytest.raises(Exception) as err:
        reminder.remind()
    error_message = str(err.value)
    assert error_message == ("No reminder set!")