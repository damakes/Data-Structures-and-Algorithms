class Queue:
    def __init__(self):
        """
        Initializes a new instance of Queue.
        """
        self.data = []

    def enqueue(self, data):
        """
        Add element to queue.

        Parameters: to be added to the queue.
        """
        self.data.append(data)

    def dequeue(self):
        """
        Returns The item removed from the queue, or None if the queue is empty.
        """
        if not self.is_empty():
            return self.data.pop(0)

    def is_empty(self):
        """
        Checks if the queue is empty.
        """
        return len(self.data) == 0

    def size(self):
        """
        Number of elements in the queue.
        """
        return len(self.data)

def get_pairs(numbers):
    """
    Checks pairs of even and odd numbers from a list of numbers.

    Returns: list of tuples, pairs of even and odd numbers.
    """
    even_queue = Queue()
    odd_queue = Queue()
    pairs = []

    for num in numbers:
        if num % 2 == 0:  # Check if the number is even
            if not odd_queue.is_empty():  # Check if there's an odd number waiting in the queue
                odd_num = odd_queue.dequeue()
                pairs.append((num, odd_num))
            else:
                even_queue.enqueue(num)
        else:  # Number is odd
            if not even_queue.is_empty():  # Check if there's an even number waiting in the queue
                even_num = even_queue.dequeue()
                pairs.append((even_num, num))
            else:
                odd_queue.enqueue(num)

    return pairs


# TESTS
def test():
  check_pairs = (get_pairs([74, 21, 18, 22, 71, 77, 82, 16, 77, 32, 90, 37, 98, 31, 59, 37, 99, 46, 28, 65]))
  q = [(74, 21), (18, 71), (22, 77), (82, 77), (16, 37), (32, 31), (90, 59), (98, 37), (46, 99), (28, 65)]
  print(check_pairs, check_pairs == q)

  q = [(36, 93), (98, 55), (26, 9), (72, 83), (48, 77), (18, 97), (20, 81), (2, 51)]
  check_pairs = (get_pairs([93, 55, 9, 36, 83, 98, 77, 97, 26, 81, 72, 48, 18, 20, 2, 88, 82, 51, 58, 30]))
  print(check_pairs, check_pairs == q)

  q = [(38, 79), (36, 71), (40, 97), (26, 91), (14, 27), (30, 71), (86, 67)]
  check_pairs = (get_pairs([79, 38, 36, 40, 26, 14, 30, 71, 97, 91, 86, 27, 71, 28, 70, 60, 70, 96, 67, 16]))
  print(check_pairs, check_pairs == q)

  q = [(36, 93), (98, 55), (26, 9), (72, 83), (48, 77), (18, 97), (20, 81), (2, 51)]
  check_pairs = (get_pairs([93, 55, 9, 36, 83, 98, 77, 97, 26, 81, 72, 48, 18, 20, 2, 88, 82, 51, 58, 30]))
  print(check_pairs, check_pairs == q)

  q = [(8, 95), (8, 61), (54, 69), (68, 43), (4, 67), (96, 23), (52, 55), (52, 5), (54, 19)]
  check_pairs = (get_pairs([8, 95, 61, 69, 43, 67, 8, 23, 55, 5, 54, 68, 4, 96, 19, 57, 52, 52, 89, 54]))
  print(check_pairs, check_pairs == q)
test()
