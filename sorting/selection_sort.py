class InsertionSort(object):

	@staticmethod
	def sort(input_data):
		for index in range(1, len(input_data)):
			item_to_sort = input_data[index]
			item_index = index
			while item_to_sort < input_data[item_index-1] and item_index > 0:
				input_data[item_index] = input_data[item_index-1]
				input_data[item_index-1] = item_to_sort
				item_index -= 1
		return input_data
