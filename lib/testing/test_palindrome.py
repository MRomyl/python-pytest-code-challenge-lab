from lib.palindrome import longest_palindromic_substring

def test_basic_cases():
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring("cbbd") == "bb"
    assert longest_palindromic_substring("racecar") == "racecar"

def test_edge_cases():
    # Empty string
    assert longest_palindromic_substring("") == ""
    # Single character
    assert longest_palindromic_substring("a") == "a"
    # No palindrome longer than 1
    assert longest_palindromic_substring("abcde") in ["a", "b", "c", "d", "e"]
    # Long string with repeating pattern
    assert longest_palindromic_substring("abacdfgdcaba") == "aba"
