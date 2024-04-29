class HashItem():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'{{{self.key}: {self.value}}}'

class HashTable():
    def __init__(self, size=256):
        self.size = size
        self.slots = [None] * size
        self.used_slots = 0

    def __repr__(self):
        text = ''
        for index, slot in enumerate(self.slots):
            if slot:
                text += f', {index}: {slot}'
        plural = '' if self.used_slots == 1 else 's'
        return f'<HashTable ({self.used_slots} element{plural}): [{text.lstrip(", ")}]'

    def _hash(self, key):
        """
        Hashing function. Can be changed for a custom one.
        """
        return len(key) % self.size

    def _find_free_slot(self, start):
        """
        Starting from 'start' find the next free slot available.

        Parameters:
        - 'start': Starting point for the search.

        Returns: The index of the next free slot or None if no free slots
        """
        # Start given position search
        current = start

        # while position is in use
        while self.slots[current]:
            # Increment current, but if the end or the table is reached,
            # continue from the start of the table.
            current = (current + 1) % self.size


            # no free positions available, return none
            if current == start:
                return None

        return current


def test():

    h = HashTable()

    for c in "abcdefghijklmnopqrstuvwxyz":
        h.slots[(ord(c) * ord(c)) % h.size] = c

    print(h._find_free_slot(0), h._find_free_slot(0) == 1)
    print(h._find_free_slot(1), h._find_free_slot(1) == 1)
    print(h._find_free_slot(10), h._find_free_slot(10) == 10)

    h = HashTable()

    for c in "abcdefghijklmnopqrstuvwxyz":
        h.slots[(ord(c) * ord(c)) % h.size] = c
        h.slots[(ord(c) * ord(c) * ord(c)) % h.size] = c
        h.slots[(ord(c) * ord(c) * ord(c) * ord(c)) % h.size] = c
        h.slots[(ord(c) * ord(c) * ord(c) * ord(c) * ord(c)) % h.size] = c
    h.slots[-1] = h.slots[-2] = 'z'

    print(h._find_free_slot(0), h._find_free_slot(0) == 1)
    print(h._find_free_slot(16), h._find_free_slot(16) == 18)
    print(h._find_free_slot(17), h._find_free_slot(17) == 18)
    print(h._find_free_slot(33), h._find_free_slot(33) == 34)
    print(h._find_free_slot(46), h._find_free_slot(46) == 46)
    print(h._find_free_slot(49), h._find_free_slot(49) == 50)
    print(h._find_free_slot(64), h._find_free_slot(64) == 66)
    print(h._find_free_slot(65), h._find_free_slot(65) == 66)
    print(h._find_free_slot(253), h._find_free_slot(253) == 253)
    print(h._find_free_slot(254), h._find_free_slot(254) == 1)
    print(h._find_free_slot(255), h._find_free_slot(255) == 1)

    h = HashTable()

    h.slots = [True] * 256
    h.slots[0] = None

    print(h._find_free_slot(0), h._find_free_slot(0) == 0)
    print(h._find_free_slot(16), h._find_free_slot(16) == 0)
    print(h._find_free_slot(17), h._find_free_slot(17) == 0)
    print(h._find_free_slot(33), h._find_free_slot(33) == 0)
    print(h._find_free_slot(46), h._find_free_slot(46) == 0)
    print(h._find_free_slot(49), h._find_free_slot(49) == 0)
    print(h._find_free_slot(64), h._find_free_slot(64) == 0)
    print(h._find_free_slot(65), h._find_free_slot(65) == 0)
    print(h._find_free_slot(253), h._find_free_slot(253) == 0)
    print(h._find_free_slot(254), h._find_free_slot(254) == 0)
    print(h._find_free_slot(255), h._find_free_slot(255) == 0)

    h = HashTable()

    h.slots = [True] * 256

    print(h._find_free_slot(0), h._find_free_slot(0) == None)
    print(h._find_free_slot(16), h._find_free_slot(16) == None)
    print(h._find_free_slot(17), h._find_free_slot(17) == None)
    print(h._find_free_slot(33), h._find_free_slot(33) == None)
    print(h._find_free_slot(46), h._find_free_slot(46) == None)
    print(h._find_free_slot(49), h._find_free_slot(49) == None)
    print(h._find_free_slot(64), h._find_free_slot(64) == None)
    print(h._find_free_slot(65), h._find_free_slot(65) == None)
    print(h._find_free_slot(253), h._find_free_slot(253) == None)
    print(h._find_free_slot(254), h._find_free_slot(254) == None)
    print(h._find_free_slot(255), h._find_free_slot(255) == None)


test()
