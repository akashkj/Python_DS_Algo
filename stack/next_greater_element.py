"""
Problem: find next greater element for each element, if not present, return -1 for such element
Solution: Push elements to stack. Iterate and pop all elements elements smaller than current element. If false or empty stack, push current to stack
		  and move to next element. Left elements at the end don't have NGE.
		  Complexity - O(n)
"""

class Stack(object):
	def __init__(self):
		self.stack = []
	
	def push(self, value):
		self.stack.append(value)
		
	def pop(self):
		temp = self.stack[-1]
		del self.stack[-1]
		return temp
		
	def empty(self):
		return not self.stack
		
	def peek(self):
		return self.stack[-1]
		
def get_next_greater_elements(elements):
	if not elements:
		return
	result = []
	s = Stack()
	s.push(elements[0])
	for current in elements[1:]:
		while not s.empty():
			if s.peek() < current:
				result.append((s.pop(), current))
			else:
				break
		s.push(current)
	while not s.empty():
		result.append((s.pop(), -1))
	return result
	
if __name__ == "__main__":
	print get_next_greater_elements([])
	print get_next_greater_elements(None)
	print get_next_greater_elements([1, 2, 3, 4])
	print get_next_greater_elements([11, 13, 3, 21])
	print get_next_greater_elements([2, 5, 3, 7, 11, 25, 6])
	print get_next_greater_elements([5, 4, 3, 2, 1])
				
			