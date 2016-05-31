#Using Kadane's algorithm

def get_maximum_sub_array_sum(input_array):
	current_sum = max_sum = input_array[0]
	start_index = end_index = 0
	for i in range(1, len(input_array)):
		num = input_array[i]
		if current_sum < max(num, current_sum + num):
			current_sum = max(num, current_sum + num)
		if current_sum == num:
			start_index = i
		if current_sum > max_sum:
			max_sum = current_sum
			end_index = i
	return input_array[start_index: end_index + 1]
	
if __name__ == '__main__':
	print get_maximum_sub_array_sum([-500])
	print get_maximum_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3])
	print get_maximum_sub_array_sum([-2, -3, -1, -2, -3])
	