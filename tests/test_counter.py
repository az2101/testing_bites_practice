

from lib.counter import *

def test_counter_works_for_five():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == 'Counted to 5.'

def test_counter_works_for_two_adds():
    counter = Counter()
    counter.add(5)
    counter.add(6)
    result = counter.report()
    assert result == 'Counted to 11.'

    

