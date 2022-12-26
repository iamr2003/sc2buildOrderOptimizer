cdef class PriorityQueue:
    cdef list heap
    cdef dict lookup

    def __init__(self):
        self.heap = []
        self.lookup = {}

    cdef void _sift_up(self, int index):
        cdef int parent = (index - 1) // 2
        cdef int priority = self.heap[index][0]
        cdef object element = self.heap[index][1]

        while index > 0 and self.heap[parent][0] > priority:
            self.heap[index] = self.heap[parent]
            self.lookup[self.heap[index][1]] = index
            index = parent
            parent = (index - 1) // 2

        self.heap[index] = (priority, element)
        self.lookup[element] = index

    cdef void _sift_down(self, int index):
        cdef int child = 2 * index + 1
        cdef int priority = self.heap[index][0]
        cdef object element = self.heap[index][1]

        while child < len(self.heap):
            if child + 1 < len(self.heap) and self.heap[child + 1][0] < self.heap[child][0]:
                child += 1

            if priority <= self.heap[child][0]:
                break

            self.heap[index] = self.heap[child]
            self.lookup[self.heap[index][1]] = index
            index = child
            child = 2 * index + 1

        self.heap[index] = (priority, element)
        self.lookup[element] = index

    def push(self, int priority, object element):
        self.heap.append((priority, element))
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        element = self.heap[0][1]
        del self.lookup[element]

        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()
            self._sift_down(0)
        else:
            self.heap.pop()

        return element

    def contains(self, object element):
        return element in self.lookup

    def get_priority(self, object element):
        return self.heap[self.lookup[element]][0]

    def set_priority(self, object element, int priority):
        index = self.lookup[element]
        old_priority = self.heap[index][0]
        self.heap[index] = (priority, element)

        if priority < old_priority:
            self._sift_up(index)
        else:
            self._sift_down(index)
