"""
Finds the length of longest increasing subsequence in a list of numbers
e.g. 1,2,3,5,4,6 length = 5
"""
def get_longest_increasing_subsequence(numbers):
	"""
	:param numbers: list of integers
	:return: integer
	"""
	input_size = len(numbers)
	if input_size in [0, 1]:
		return input_size
	result = [1] * input_size #Every element is a increasing subsequence of length 1 if considered individually
	max_length = 0
	for i in range(input_size):
		for j in range(0, i):
			if numbers[j] < numbers[i]:
				result[i] = max(result[i], result[j] + 1)
				max_length = max(max_length, result[i])
	return max_length
	
	
if __name__ == "__main__":
	assert get_longest_increasing_subsequence([]) == 0
	assert get_longest_increasing_subsequence([3]) == 1
	assert get_longest_increasing_subsequence([1, 2, 3]) == 3
	assert get_longest_increasing_subsequence([3, 5, 89, 2, 4, 7, 8, 6]) == 4
	assert get_longest_increasing_subsequence([500, 23, 24, 25, 19, 11, 13, 14, 15, 17, 16]) == 5
	