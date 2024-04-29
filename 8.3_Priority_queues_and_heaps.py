def binary_search_iterative(array, value):
    """
    Performs a binary search in the the array for the given value

    Parameters:
    - array: The array where to perform the search
    - value: The value being searched

    Returns: The index of the value if it is found.
             Or None if it is not found.
    """
    # Search the whole array.
    start = 0
    end = len(array) - 1

    # While start var is on left of end var
    while start <= end:
        # Calculate the midpoint
        midpoint = start + (end - start + 1) // 2

        # value found in midpoint, return index
        if array[midpoint] == value:
            return midpoint

        # searched value is smaller, than the one in the midpoint
        if value < array[midpoint]:
            # move the end to the left, before the midpoint
            end = midpoint - 1

        # searched value is bigger, than the one in the midpoint
        if value > array[midpoint]:
            # move the start to the right, after the midpoint
            start = midpoint + 1

    return None





def test():
  array = [1, 2, 3]
  print(binary_search_iterative(array, 2) == 1)

  array = [0, 5, 8, 11, 14, 17, 29, 31, 31, 35, 39, 40, 47, 61, 68, 78, 85, 88, 95, 98]
  print(binary_search_iterative(array, 0)==0)
  print(binary_search_iterative(array, 98)==19)
  print(binary_search_iterative(array, 29)==6)
  print(binary_search_iterative(array, 100)==None)
  print(binary_search_iterative(array, -1)==None)
  print(binary_search_iterative(array, 44)==None)

test()
