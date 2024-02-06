"""
This is an example of how you could unit test specific functions/helper functions
"""


def test_rev_str():
    """Example of importing a function to do a unit test"""
    from app import rev_str

    assert rev_str("hello") == "olleh", "Should reverse a normal string"
    assert rev_str("") == "", "Should handle empty string"
    assert rev_str("12345") == "54321", "Should reverse numeric strings"
    assert (
        rev_str("hello, hi!") == "!ih ,olleh"
    ), "Should reverse strings with punctuation and spaces"
