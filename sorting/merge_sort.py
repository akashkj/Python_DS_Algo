class MergeSort(object):

	@staticmethod
	def sort(data_to_sort):
		input_size = len(data_to_sort)
		if input_size < 2:
			return data_to_sort
		mid = input_size / 2 
		left_data = data_to_sort[:mid]
		right_data = data_to_sort[mid:]
		left_data = MergeSort.sort(left_data)
		right_data = MergeSort.sort(right_data)
		return MergeSort._merge(left_data, right_data)
		
	@staticmethod
	def _merge(left_data, right_data):
		sorted_data = []
		i, j = 0, 0
		len_left_data = len(left_data)
		len_right_data = len(right_data)
		while i < len_left_data and j < len_right_data:
			if left_data[i] < right_data[j]:
				sorted_data.append(left_data[i])
				i += 1
			else:
				sorted_data.append(right_data[j])
				j += 1
		if i < len_left_data:
			for data in left_data[i:]:
				sorted_data.append(data)
		if j < len_right_data:
			for data in left_data[j:]:
				sorted_data.append(data)
		return sorted_data


if __name__ == '__main__':
    print MergeSort.sort([4, 5, 23, 67, 1, 9])