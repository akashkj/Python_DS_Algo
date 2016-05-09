class BinarySearch(object):
		
	def search_element(self, data_to_be_searched, query, low, high):
		dataset_length = len(data_to_be_searched)
		if dataset_length == 0:
			return None
		while low != high:
			mid = (low + high) / 2
			if data_to_be_searched[mid] == query:
				return mid
			if data_to_be_searched[mid] > query:
				self.search_element(data_to_be_searched, query, 0, mid - 1)
			else:
				self.search_element(data_to_be_searched, query, mid, dataset_length - 1)
		