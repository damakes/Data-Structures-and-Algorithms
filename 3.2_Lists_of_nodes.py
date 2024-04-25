class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<ListNode: {self.data}>'

class SinglyLinkedList():
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<SinglyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size

    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value
        new_node = ListNode(value)

        # If list is empty just point the header to the new node
        if not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            # if list is not empty, update the last element and point it to the new node
            self._tail.next = new_node
            self._tail = new_node

        # Update list's size
        self._size += 1

    def pop(self):
        """
        Removes the last node of the list

        Parameters: None

        Returns:
            The content of the removed node. If list is empty, returns None
        """
        # If list is empty return None
        if not self._size:
            return None

        # Locate previous_node (the node just before last node)
        if self._size == 1:
            previous_node = None
        else:
            previous_node = self._head
            for _ in range(self._size-2):
                    previous_node = previous_node.next
        node_to_remove = self._tail
        # If node to remove is the first node, then update head
        if previous_node is None:
            self._head = None
        else:
            # If not, update previous node
            previous_node.next = None

        # Update tail
        self._tail = previous_node
        # Update size, remove node and return its content
        self._size -= 1
        value = node_to_remove.data
        del(node_to_remove)
        return value


# test
def test_pop():
    mylist = SinglyLinkedList()
    for c in 'abc':
        mylist.append(c)
    val = mylist.pop()
    print(val, mylist,(str(f'{val} {mylist}') == 'c <SinglyLinkedList (2 elements): [a, b]>'))

    mylist = SinglyLinkedList()
    for c in 'abc':
        mylist.append(c)
    val = mylist.pop()
    mylist.append('c')
    mylist.append('d')
    val = mylist.pop()
    print(val, mylist,(str(f'{val} {mylist}') == 'd <SinglyLinkedList (3 elements): [a, b, c]>'))


    mylist = SinglyLinkedList()
    for c in 'ab':
        mylist.append(c)
    val = mylist.pop()
    print(val, mylist,(str(f'{val} {mylist}') == 'b <SinglyLinkedList (1 element): [a]>'))

    mylist = SinglyLinkedList()
    mylist.append('a')
    val = mylist.pop()
    print(val, mylist,(str(f'{val} {mylist}') == 'a <SinglyLinkedList (0 elements): []>'))


    mylist = SinglyLinkedList()
    val = mylist.pop()
    print(val, mylist,(str(f'{val} {mylist}') == 'None <SinglyLinkedList (0 elements): []>'))

test_pop()
