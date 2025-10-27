def longest_palindromic_substring(s: str) -> str:
    if not s:
        return ""

    start = 0
    end = 0

    for i in range(len(s)):
        # Odd length
        len1 = expand_from_center(s, i, i)
        # Even length
        len2 = expand_from_center(s, i, i + 1)
        max_len = max(len1, len2)

        if max_len > (end - start):
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]


def expand_from_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1
