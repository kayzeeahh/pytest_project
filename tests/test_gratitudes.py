from lib.gratitudes import *

# Test for when there is a gatetitude
def test_for_gratitudes_in_list():
    gratitude = Gratitudes()
    gratitude.add("health")
    result = gratitude.format()
    assert result == "Be grateful for: health"

# test for no gratitude

def test_for_no_gratitude_in_list():
    gratitude = Gratitudes()
    gratitude.add("")
    result = gratitude.format()
    assert result == "Be grateful for: "
    
# test for multiple gratitudes

def test_for_multiple_gratitudes_in_list():
    gratitude = Gratitudes()
    gratitude.add("life, family, friends")
    result = gratitude.format()
    assert result == "Be grateful for: life, family, friends"