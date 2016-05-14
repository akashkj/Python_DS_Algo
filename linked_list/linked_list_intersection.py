def get_linked_list_length(x):
	length = 0
	while x:
		length += 1
		x = x.next
	return length

def get_intersection_node(A, B):
	len_a = get_linked_list_length(A)
	len_b = get_linked_list_length(B)
	a = A
	b = B
	while a and b:
		if len_a < len_b:
			b = b.next
			len_b -= 1
		elif len_b < len_a:
			a = a.next
			len_a -= 1
		else:
			if a == b:
				return a
			a = a.next
			b = b.next
	return None