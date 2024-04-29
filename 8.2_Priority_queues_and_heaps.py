class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        # Start at the end of the heap
        index = self._size - 1
        # Calculate index of parent element
        parent_index = (index-1) // 2
        # While not at Root node and value less than its parent
        while index > 0 and self._heap[index] < self._heap[parent_index]:
            # swap value with its parent
            self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
            # Update indices
            index = parent_index
            parent_index = (index-1) // 2

    def insert(self, value):
        # Add the value to the heap
        self._heap.append(value)
        # Update size of the heap
        self._size += 1
        # And float the last element of the heap
        self._float()

    def _sink(self):
        """
        Sinks the root node of the heap until the heap is in order
        """
        index = 0
        # While node has at least one child
        while index*2+1 < self._size:
            if index*2+2 < self._size:
                # If two children
                child_node_index = min(index*2+1, index*2+2, key=lambda x: self._heap[x])
            else:
                # If only one child
                child_node_index = index*2+1
            # compare the child with its parent
            if self._heap[index] > self._heap[child_node_index]:
                 # swap the values if the parent is bigger than the child.
                self._heap[index], self._heap[child_node_index] = self._heap[child_node_index], self._heap[index]
                index = child_node_index
            else:
                break


def test_sink():
  h = Heap()
  h._heap = [8, 6, 5, 9, 7]
  h._size = 5
  h._sink()
  print(h._heap == [5, 6, 8, 9, 7])

  h = Heap()
  h._heap = [8, 5, 6, 9, 7]
  h._size = 5
  h._sink()
  print(h._heap == [5, 7, 6, 9, 8])



  h = Heap()
  h._heap = [8]
  h._size = 1
  h._sink()
  print(h._heap == [8])

  h = Heap()
  h._heap = [8, 9]
  h._size = 2
  h._sink()
  print(h._heap == [8, 9])

  h = Heap()
  h._heap = [9, 8]
  h._size = 2
  h._sink()
  print(h._heap == [8, 9])

  h = Heap()
  h._heap = [25, 10, 20, 30, 40, 50, 60]
  h._size = 7
  h._sink()
  print(h._heap == [10, 25, 20, 30, 40, 50, 60])

test_sink()
