"""
Implementation of stack data structure
"""
class Stack(object):

	def __init__(self):
		self._stack = []
		
	def push(self, value):
		"""
		Adds an element to the stack at the end
		:param value: value to be inserted in the stack
		"""
		self._stack.append(value)
		
	def pop(self):
		"""
		Removed an element from stack at the end
		:return: value that is removed from the stack
		"""
		popped_element = None if len(self._stack) == 0 else self._stack[-1]
		if popped_element:
			del self._stack[-1]
		return popped_element
		
	def is_empty(self):
		"""
		Checks if stack is empty
		:return: boolean if stack is empty
		"""
		return len(self._stack) == 0
		
	def show(self):
		"""
		Gives stack content
		:return: list with stack contents
		"""
		return self._stack
		
		
if __name__ == "__main__":
	st = Stack()
	st.push(3)
	print st.show()
	st.push(4)
	print st.show()
	st.pop()
	print st.show()
	st.pop()
	print st.show()
	st.pop()
	print st.show()
	print st.is_empty()