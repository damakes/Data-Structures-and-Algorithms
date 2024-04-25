class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<ListNode: {self.data}>'

class SinglyLinkedList():
    def __init__(self):
        self._head = None

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        return f'<SinglyLinkedList: [{values.lstrip(", ")}]>'

    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value
        node = ListNode(value)
        # If list is empty just point the header to the new node
        if not self._head:
            self._head = node
        else:
            # if list is not empty, search for the last element and point it to the new node
            current_node = self._head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = node

    def pop(self):
        # If list is empty return None
        if self._head is None:
            return None

        # Get last nodes
        current_node = self._head
        prev_node = None

        # Traverse the list until the last node
        while current_node.next:
            prev_node = current_node
            current_node = current_node.next

        # Update pointers to remove the last node
        if self._head == current_node:
            self._head = None
        else:
            prev_node.next = None

        # Update size, remove node, and return its content
        value = current_node.data
        del current_node

        return value

# TEST
def test_pop():

    mylist = SinglyLinkedList()
    for i in 'abc':
        mylist.append(i)
    val = mylist.pop()
    print(val, mylist,(str(f'{val} {mylist}') == 'c <SinglyLinkedList: [a, b]>'))

    mylist = SinglyLinkedList()
    for i in 'ab':
        mylist.append(i)
    val = mylist.pop()
    print(val, mylist,(str(f'{val} {mylist}') == 'b <SinglyLinkedList: [a]>'))

    mylist = SinglyLinkedList()
    mylist.append('a')
    val = mylist.pop()
    print(val, mylist,(str(f'{val} {mylist}') == 'a <SinglyLinkedList: []>'))

    mylist = SinglyLinkedList()
    val = mylist.pop()
    print(val, mylist,(str(f'{val} {mylist}') == 'None <SinglyLinkedList: []>'))

test_pop()
