class StackBasedQueue:
    def __init__(self):
        # YOUR CODE HERE
        self._size = 0
        self._InboundStack = []
        self._OutboundStack = []

    def __repr__(self):
        """
        Returns a string representation of the queue.

        Returns: size of the queue and its elements.
        """
        plural = '' if self._size == 1 else 's'
        values = [c for c in self._OutboundStack]
        values.extend([c for c in self._InboundStack][::-1])
        return f'<StackBasedQueue ({self._size} element{plural}): [{", ".join(values)}]>'

    def enqueue(self, item):
        """
        Adds an element to the rear of the queue.

        Parameters: item: The item to be added to the queue.
        """
        # YOUR CODE HERE
        self._InboundStack.append(item)
        self._size += 1

    def dequeue(self):
        """
        Removes and returns the element at the front of the queue.

        Returns: removed item from the queue.
        """
        # YOUR CODE HERE
        if not self._OutboundStack:
            # Transfer elements from Inbound to Outbound stack
            while self._InboundStack:
                self._OutboundStack.append(self._InboundStack.pop())
        if self._OutboundStack:
            self._size -= 1
            return self._OutboundStack.pop()


# TESTS
def test():
    queue = StackBasedQueue()
    print(queue, (str(queue) == '<StackBasedQueue (0 elements): []>'))

    queue = StackBasedQueue()
    queue.enqueue('A')
    print(queue, (str(queue) == '<StackBasedQueue (1 element): [A]>'))

    queue = StackBasedQueue()
    queue.enqueue('A')
    queue.enqueue('B')
    print(queue, (str(queue)== '<StackBasedQueue (2 elements): [B, A]>'))

    queue = StackBasedQueue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    print(queue, (str(queue) == '<StackBasedQueue (3 elements): [C, B, A]>'))

    queue = StackBasedQueue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    val = queue.dequeue()
    print(val, queue,(str(f'{val} {queue}') == 'A <StackBasedQueue (2 elements): [C, B]>'))

    queue = StackBasedQueue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    val = queue.dequeue()
    val = queue.dequeue()
    print(val, queue,(str(f'{val} {queue}') == 'B <StackBasedQueue (1 element): [C]>'))

    queue = StackBasedQueue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    val = queue.dequeue()
    val = queue.dequeue()
    val = queue.dequeue()
    print(val, queue,(str(f'{val} {queue}') == 'C <StackBasedQueue (0 elements): []>'))


    queue = StackBasedQueue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    val = queue.dequeue()
    val = queue.dequeue()
    val = queue.dequeue()
    val = queue.dequeue()
    print(val, queue,(str(f'{val} {queue}') == 'None <StackBasedQueue (0 elements): []>'))
test()
