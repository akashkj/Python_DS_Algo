"""
Computes length of longest common subsequence between two strings
"""


def lcs_length(input_1, input_2):
    """
    Computes length of longest common subsequence between two strings
    :param input_1: first string
    :param input_2: second string
    :return: integer length of longest common subsequence
    """
    row_count = len(input_1) + 1
    col_count = len(input_2) + 1
    dp = [[0 for _ in range(col_count)] for _ in range(row_count)]
    for i in range(row_count):
        for j in range(col_count):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif input_1[i - 1] == input_2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp[row_count - 1][col_count - 1]

if __name__ == "__main__":
    assert 0 == lcs_length("abc", "xyz")
    assert 4 == lcs_length("abcd", "abcd")
    assert 4 == lcs_length("abcdef", "sdfsdfcdefsdgds")
    assert 7 == lcs_length("abcxxabcd", "abcyyabcd")

