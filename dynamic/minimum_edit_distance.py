def get_minimum_edit_distance(A, B):
	size_a = len(A)
	size_b = len(B)
	result = [[0 for i in range(size_b + 1)] for _ in range(size_a + 1)]
	for i in range(size_a + 1):
		for j in range(size_b + 1):
			if i == 0:
				result[i][j] = j
			elif j == 0:
				result[i][j] = i
			elif A[i - 1] == B[j - 1]:
				result[i][j] = result[i-1][j-1]
			else:
				result[i][j] = min(result[i-1][j], result[i-1][j-1], result[i][j-1]) + 1
	return result[-1][-1]
	
print get_minimum_edit_distance("abc", "xyz")
print get_minimum_edit_distance("abc", "abc")
print get_minimum_edit_distance("", "xyz")
print get_minimum_edit_distance("abc", "")
print get_minimum_edit_distance("abc", "abcd")
print get_minimum_edit_distance("abcsdsdh", "asjfsgk")
				
				