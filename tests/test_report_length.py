from lib.report_length import report_length

def test_report_length_of_given_string():
    result = report_length("hello")
    assert result == "This string was 5 characters long"

