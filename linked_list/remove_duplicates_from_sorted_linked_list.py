def remove_duplicates(head):
	if not head:
		return None
	current = head
	while current.next:
		while current.data == current.next.data:
			if current.next.next:
				current.next = current.next.next
			else:
				current.next = None
				return head
		current = current.next
	return head