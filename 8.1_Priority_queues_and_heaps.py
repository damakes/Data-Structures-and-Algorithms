class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        """
        Float the last element of the heap until the heap is in order
        """
        child_node_index = self._size - 1

        while child_node_index > 0:
            # find the parent index
            parent_index = (child_node_index - 1) // 2 # Calculate the parent index
            # compare the node with its parent
            if self._heap[child_node_index] < self._heap[parent_index]:
              # swap the values if the child node is bigger than the parent.
                self._heap[child_node_index], self._heap[parent_index] = self._heap[parent_index], self._heap[child_node_index]
                child_node_index = parent_index
            else:
                break



# tests
def test_float():

  h = Heap()
  h._heap = [3, 6, 5, 9, 7, 8, 2]
  h._size = 7
  h._float()
  print(h._heap, h._heap == [2, 6, 3, 9, 7, 8, 5])

  h = Heap()
  h._heap = [3, 6, 5, 9, 7, 8, 4]
  h._size = 7
  h._float()
  print(h._heap, h._heap == [3, 6, 4, 9, 7, 8, 5])

  h = Heap()
  h._heap = [3]
  h._size = 1
  h._float()
  print(h._heap ,h._heap == [3])

  h = Heap()
  h._heap = [3, 4]
  h._size = 2
  h._float()
  print(h._heap ,h._heap == [3, 4])

  h = Heap()
  h._heap = [4, 3]
  h._size = 2
  h._float()
  print(h._heap ,h._heap == [3, 4])

test_float()
