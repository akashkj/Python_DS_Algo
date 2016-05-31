#Using Kadane's algorithm

def get_maximum_sub_array_sum(input_array):
	current_sum = max_sum = input_array[0]
	for num in input_array[1:]:
		current_sum = max(num, current_sum + num)
		max_sum = max(max_sum, current_sum)
	return max_sum
	
if __name__ == '__main__':
	print get_maximum_sub_array_sum([-500])
	print get_maximum_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3])
	print get_maximum_sub_array_sum([-2, -3, -1, -2, -3])
	