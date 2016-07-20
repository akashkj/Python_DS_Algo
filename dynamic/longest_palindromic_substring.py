"""
In a given string, find length of the longest substring that is a palindrome
Solution: Reverse the string and apply longest common substring on original and reversed string
"""


def _get_longest_common_substring(input_1, input_2):
    result = [[0 for _ in range(len(input_1) + 1)] for _ in range(len(input_2) + 1)]
    max_length = 1
    for i in range(1, len(input_1) + 1):
        for j in range(1, len(input_2) + 1):
            if input_1[i - 1] == input_2[j - 1]:
                result[i][j] = result[i - 1][j - 1] + 1
            else:
                result[i][j] = 0
            max_length = max(max_length, result[i][j])
    return max_length if max_length > 1 else 0


def get_length_of_longest_palindrome(input_string):
    if not input_string:
        return 0
    reversed_string = input_string[::-1]
    return _get_longest_common_substring(input_string, reversed_string)

if __name__ == '__main__':
    assert get_length_of_longest_palindrome(None) == 0
    assert get_length_of_longest_palindrome("") == 0
    assert get_length_of_longest_palindrome("abc") == 0
    assert get_length_of_longest_palindrome("abcbd") == 3
    assert get_length_of_longest_palindrome("abcddcba") == 8
    assert get_length_of_longest_palindrome("abatedqwertyytrewq") == 12

