"""
Stack data structure that can perform push(), pop(), peek() and minimum() operations in O(1) time
Solution: Create an auxilary stack to store minimum element at the top for all operations
"""


class Stack(object):

    def __init__(self):
        self._content = []
        self._auxiliary = []

    def push(self, value):
        """
        :param value: homogeneous objects
        """
        if value is None:
            raise AttributeError("None is not a supported type")
        self._content.append(value)
        self._push_to_auxiliary(value)

    def pop(self):
        """
        Deletes the element at the top of the stack
        :return: deleted object
        """
        if len(self._content) == 0:
            return None
        popped_entry = self._content[-1]
        del self._content[-1]
        del self._auxiliary[-1]
        return popped_entry

    def peek(self):
        """
        Provides the element at the top of stack but doesn't delete tit
        :return: object at the top of stack
        """
        if len(self._content) == 0:
            return None
        return self._content[-1]

    def minimum(self):
        """
        Provides minimum element in the stack
        :return: object minimum value in stack
        """
        if len(self._content) == 0:
            return None
        return self._auxiliary[-1]

    def show(self):
        """
        Prints the stack content
        """
        for entry in self._content:
            print entry,

    def get_stack(self):
        """
        Provides stack content
        :return: list having stack elements
        """
        return self._content

    def _push_to_auxiliary(self, value):
        """
        Updates top of auxiliary stack with the minimum
        :param value: valid object
        """
        if not self._auxiliary:
            self._auxiliary.append(value)
        else:
            self._auxiliary.append(min(self._auxiliary[-1], value))


if __name__ == '__main__':
    s = Stack()
    assert s.pop() is None
    assert len(s.get_stack()) == 0
    s.push(3)
    assert len(s.get_stack()) == 1
    assert s.minimum() == 3
    assert s.pop() == 3
    assert len(s.get_stack()) == 0
    s.push(7)
    assert s.minimum() == 7
    s.push(5)
    assert s.minimum() == 5
    s.push(10)
    assert s.minimum() == 5
    s.pop()
    assert s.minimum() == 5
