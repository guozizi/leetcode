class Array:
    def __init__(self, size=32, init=None):
        self._size = size
        self._items = [init] * size

    def __getitem__(self, item):
        return self._items[item]

    def __setitem__(self, key, value):
        self._items[key] = value

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __delitem__(self, key):
        del self._items[key]

    def __iter__(self):
        for item in self._items:
            yield item


class MaxHeap(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception('full')
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count - 1)

    def _siftup(self, ndx):
        if ndx > 0:
            parent = int((ndx - 1) / 2)
            if self._elements[ndx] > self._elements[parent]:
                self._elements[ndx], self._elements[parent] = self._elements[parent], self._elements[ndx]
                self._siftup(parent)

    def extract(self):
        if self._count <= 0:
            raise Exception('empty')
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        self._siftdown(0)
        return value

    def _siftdown(self, ndx):
        left = 2 * ndx + 1
        right = 2 * ndx + 2
        largest = ndx

        if (left < self._count and
                self._elements[left] >= self._elements[largest] and
                self._elements[left] >= self._elements[right]):
            largest = left

        elif right < self._count and self._elements[right] >= self._elements[largest]:
            largest = right

        if largest != ndx:
            self._elements[ndx], self._elements[largest] = self._elements[largest], self._elements[ndx]
            self._siftdown(largest)


def test_max_heap():
    import random
    n = 5
    h = MaxHeap(n)
    for i in range(n):
        h.add(i)
    for i in reversed(range(n)):
        assert i == h.extract()


test_max_heap()


def heapsort_reverse(array):
    length = len(array)
    maxheap = MaxHeap(length)
    for i in array:
        maxheap.add(i)
    res = []
    for i in range(length):
        res.append(maxheap.extract())
    return res


def test_heapsort_reverse():
    import random
    l = list(range(10))
    random.shuffle(l)
    assert heapsort_reverse(l) == sorted(l, reverse=True)


test_heapsort_reverse()
