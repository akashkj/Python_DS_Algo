import unittest
from linked_list.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

		
	def test_linked_list_creation(self):
		list = [1, 2, 3]
		result = LinkedList().create_linked_list_from_list(list)
		self.assertEqual(list, TestLinkedList._get_list_from_linked_list(result))
		list = []
		result = LinkedList().create_linked_list_from_list(list)
		self.assertEqual(list, TestLinkedList._get_list_from_linked_list(result))
		
	def test_remove_duplicates_from_ascending_linked_list(self):
		from linked_list.remove_duplicates_from_sorted_linked_list import remove_duplicates
		list = []
		linked_list = LinkedList().create_linked_list_from_list(list)
		result = remove_duplicates(linked_list)
		self.assertEqual(list, TestLinkedList._get_list_from_linked_list(result))
		list = [3, 3, 2]
		linked_list = LinkedList().create_linked_list_from_list(list)
		result = remove_duplicates(linked_list)
		self.assertEqual([3, 2], TestLinkedList._get_list_from_linked_list(result))
		list = [1, 1]
		linked_list = LinkedList().create_linked_list_from_list(list)
		result = remove_duplicates(linked_list)
		self.assertEqual([1], TestLinkedList._get_list_from_linked_list(result))
		list = [7, 7, 7, 7, 7, 7]
		linked_list = LinkedList().create_linked_list_from_list(list)
		result = remove_duplicates(linked_list)
		self.assertEqual([7], TestLinkedList._get_list_from_linked_list(result))
		list = [11, 13, 13, 20, 20, 20, 20, 20, 81, 81, 90]
		linked_list = LinkedList().create_linked_list_from_list(list)
		result = remove_duplicates(linked_list)
		self.assertEqual([11, 13, 20, 81, 90], TestLinkedList._get_list_from_linked_list(result))
		
		
	@staticmethod
	def _get_list_from_linked_list(linked_list):
		result = []
		while linked_list:
			result.append(linked_list.data)
			linked_list = linked_list.next
		return result