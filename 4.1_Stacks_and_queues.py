class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<Node: {self.data}>'


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def peek(self):
        """
        Returns the value of the top node without altering the stack
        """
        return self._top.data if self._top else None

    def push(self, data):
        """
        Add an element to the stack

        Parameters:
        - 'data': Data/value being added

        Returns: None
        """
        # YOUR CODE HERE.
        new_node = Node(data)
        new_node.next = self._top
        self._top = new_node
        self._size += 1

    def pop(self):
        """
        Remove the top node from the stack and return its content

        Parameters: None

        Returns: The content of the node or None if stack is empty
        """
        # YOUR CODE HERE.
        if self._top is None:
            return None

        top_node_to_remove = self._top.data
        self._top = self._top.next
        self._size -= 1

        return top_node_to_remove

    def __repr__(self):
        # YOUR CODE HERE.
        current_node = self._top
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<Stack ({self._size} element{plural}): [{values.lstrip(", ")}]>'



# TESTS
def test_push_pop():
  mystack = Stack()
  mystack.push('A')
  print(mystack,(str(f'{mystack}') == '<Stack (1 element): [A]>'))

  mystack = Stack()
  mystack.push('A')
  print(mystack,(str(f'{mystack}') == '<Stack (1 element): [A]>'))

  mystack = Stack()
  mystack.push('A')
  mystack.push('B')
  print(mystack,(str(f'{mystack}') == '<Stack (2 elements): [B, A]>'))


  mystack = Stack()
  mystack.push('A')
  mystack.push('B')
  mystack.push('C')
  print(mystack,(str(f'{mystack}') == '<Stack (3 elements): [C, B, A]>'))

  mystack = Stack()
  for c in 'ABC':
      mystack.push(c)
  val = mystack.pop()
  print(mystack,(str(f'{val} {mystack}') == 'C <Stack (2 elements): [B, A]>'))


  mystack = Stack()
  for c in 'ABC':
      mystack.push(c)
  val = mystack.pop()
  val = mystack.pop()
  print(val, mystack,(str(f'{val} {mystack}') == 'B <Stack (1 element): [A]>'))

  mystack = Stack()
  for c in 'ABC':
      mystack.push(c)
  val = mystack.pop()
  val = mystack.pop()
  val = mystack.pop()
  print(val, mystack,(str(f'{val} {mystack}') == 'A <Stack (0 elements): []>'))


  mystack = Stack()
  val = mystack.pop()
  print(val, mystack,(str(f'{val} {mystack}') == 'None <Stack (0 elements): []>'))

test_push_pop()
