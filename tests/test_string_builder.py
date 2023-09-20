from lib.string_builder import *

# Initially the output is an empty string
def test_initially_output_is_an_empty_string():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

# When we add a single string. The output is now that string.
def test_adding_a_string_outputs_that_string():
    string_builder = StringBuilder()
    string_builder.add("World")
    assert string_builder.output() == "World"
    
# When we the size reflects the size of the string
def test_adding_a_string_outputs_that_string():
    string_builder = StringBuilder()
    string_builder.add("World")
    assert string_builder.size() == 5
    
    