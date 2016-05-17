def compare_linked_lists(list_1, list_2):
	while list_1 and list_2:
		if list_1.val != list_2.val:
			return 1 if list_1.val > list_2.val else -1
		list_1 = list_1.next
		list_1 = list_2.next
	if not list_1 and not list_2:
		return 0
	return 1 if list_1 else -1