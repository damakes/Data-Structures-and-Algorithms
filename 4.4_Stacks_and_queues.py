class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
# YOUR CODE
class Queue:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def enqueue(self, data):
        """
        Add an element to rear of the queue.

        Parameters: data: The data to be added to the queue.

        Returns: None
        """
        new_node = ListNode(data)
        # If empty, set front and rear to the new node
        if self._front is None:
            self._front = new_node
            self._rear = new_node
        # add the new node to the rear and update rear
        else:
            self._rear.next = new_node
            self._rear = new_node
        self._size += 1

    def dequeue(self):
        """
        Removes and returns the element at the front of the queue.

        Returns: removed data of element, or None.
        """
        # If empty, return None
        if self._front is None:
            return None
        # remove the _front node and update _front
        else:
          data = self._front.data
          self._front = self._front.next
          self._size -= 1
          return data

    def __repr__(self):
        """
        Returns a string representation of the queue.

        Returns: size of the queue and its elements.
        """
        elements = []
        current = self._front
        plural = '' if self._size == 1 else 's'
        while current:
            # Traverse the queue and collect elements
            elements.insert(0, current.data) # Insert elements at the beginning for correct order
            current = current.next
        return f'<Queue ({self._size} element{plural}): [{", ".join(elements)}]>'



#TEST
def test():
    queue = Queue()
    print(queue,(str(f'{queue}') == '<Queue (0 elements): []>'))

    queue = Queue()
    queue.enqueue('A')
    print(queue,(str(f'{queue}') == '<Queue (1 element): [A]>'))

    queue = Queue()
    queue.enqueue('A')
    queue.enqueue('B')
    print(queue,(str(f'{queue}') == '<Queue (2 elements): [B, A]>'))


    queue = Queue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    print(queue,(str(f'{queue}') == '<Queue (3 elements): [C, B, A]>'))

    queue = Queue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    val = queue.dequeue()
    val = queue.dequeue()
    print(val,queue,(str(f'{val} {queue}') == 'B <Queue (1 element): [C]>'))

    queue = Queue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    val = queue.dequeue()
    val = queue.dequeue()
    val = queue.dequeue()
    print(val,queue,(str(f'{val} {queue}') == 'C <Queue (0 elements): []>'))

    queue = Queue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    val = queue.dequeue()
    val = queue.dequeue()
    val = queue.dequeue()
    val = queue.dequeue()
    print(val,queue,(str(f'{val} {queue}') == 'None <Queue (0 elements): []>'))
test()























# TESTS
