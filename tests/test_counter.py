from lib.counter import *

def test_count_to_five():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."
    
def test_count_to_ten():
    counter = Counter()
    counter.add(10)
    result = counter.report()
    assert result == "Counted to 10 so far."