def interpolation_search(array, value, start=None, end=None):
    """
    Performs an Interpolation search in the the array for the given value

    Parameters:
    - array: The array where to perform the search
    - value: The value being searched

    Returns: The index of the value if it is found.
             Or None if it is not found.
    """
    if start is None:
        start = 0
    if end is None:
        end = len(array) - 1

    # Calculate the midpoint
    midpoint = start + int((end - start) * ((value-array[start])/(array[end]-array[start])))

    # calculated midpoint is not within the search area
    if midpoint < start or midpoint > end:
        return None

    # value found at the midpoint, return the index of midpoint
    if array[midpoint] == value:
        return midpoint

    # searched value is smaller, than the one in the midpoint,
    # at least one element left to the midpoint
    if value < array[midpoint] and midpoint >= start+1:
        # search on left part
        return interpolation_search(array, value, start=start, end=midpoint-1)

    # searched value is bigger, than the one in the midpoint
    # at least one element right to the midpoint
    if value > array[midpoint] and midpoint <= end-1:
        # search on right part
        return interpolation_search(array, value, start=midpoint+1, end=end)

    return None


def test():
  array = [1, 2, 3]
  print(interpolation_search(array, 2) == 1)

  array = [0, 5, 8, 11, 14, 17, 29, 31, 31, 35, 39, 40, 47, 61, 68, 78, 85, 88, 95, 98]
  print(interpolation_search(array, 0)==0)
  print(interpolation_search(array, 98)==19)
  print(interpolation_search(array, 29)==6)
  print(interpolation_search(array, 100)==None)
  print(interpolation_search(array, -1)==None)
  print(interpolation_search(array, 44)==None)
test()
