# generated with chatgpt and edited by Ibrahim in collaboration

# feature request - ability for things to be unindexed, perhaps an input of None string or something
cdef class PriorityQueue:
    cdef list heap  # list of (priority, key) tuples
    cdef dict lookup  # mapping from key to element
    cdef dict key_index  # mapping from key to index in heap

    def __init__(self):
        self.heap = []
        self.lookup = {}
        self.key_index = {}

    cdef void _sift_up(self, int index):
        cdef int parent = (index - 1) // 2
        cdef int priority = self.heap[index][0]  # priority of current element
        cdef str key = self.heap[index][1]  # key of current element

        while index > 0 and self.heap[parent][0] > priority:  # while element is not root and has higher priority than parent
            self.heap[index] = self.heap[parent]  # swap elements
            self.key_index[self.heap[index][1]] = index  # update key_index for element that was swapped
            index = parent  # update
            parent = (index - 1) // 2
            self.heap[index] = (priority, key)  # place element in correct position
            self.key_index[key] = index  # update key_index for element that was moved

    cdef void _sift_down(self, int index):
        cdef int child = 2 * index + 1
        cdef int priority = self.heap[index][0]  # priority of current element
        cdef str key = self.heap[index][1]  # key of current element

        while child < len(self.heap):  # while element has at least one child
            # find child with lower priority
            if child + 1 < len(self.heap) and self.heap[child + 1][0] < self.heap[child][0]:
                child += 1

            if priority <= self.heap[child][0]:  # if current element has lower or equal priority than both children, we're done
                break

            self.heap[index] = self.heap[child]  # swap elements
            self.key_index[self.heap[index][1]] = index  # update key_index for element that was swapped
            index = child  # update index and child
            child = 2 * index + 1

        self.heap[index] = (priority, key)  # place element in correct position
        self.key_index[key] = index  # update key_index for element that was moved


    def push(self, str key, int priority, object element):
        self.heap.append((priority, key))  # add element to end of heap
        self._sift_up(len(self.heap) - 1)  # sift element up to maintain heap property

        #optional key usage is not currently possible
        self.lookup[key] = element  # add element to lookup dictionary
        self.key_index[key] = len(self.heap) - 1  # add key to key_index dictionary

    def pop(self):
        key = self.heap[0][1]  # key of element at top of heap
        element = self.lookup[key]  # element at top of heap
        del self.lookup[key]  # remove element from lookup dictionary
        del self.key_index[key]  # remove key from key_index dictionary

        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()  # replace top element with element at bottom of heap
            self.key_index[self.heap[0][1]] = 0  # update key_index for element that was moved
            self._sift_down(0)  # sift element down to maintain heap property
        else:
            self.heap.pop()

        return element

    def contains(self, str key):
        return key in self.lookup

    def get(self, str key):
        if self.contains(key):
            return self.lookup[key]
        else:
            return None

    def set_priority(self, str key, int priority):
        if self.contains(key):
            index = self.key_index[key]
            pair = self.heap[index]
            old_priority = pair[0]
            self.heap[index] = (priority, pair[1])

            if priority < old_priority:
                self._sift_up(index)
            else:
                self._sift_down(index)

    def remove(self, str key):
        if self.contains(key):
            index = self.key_index[key]
            pair = self.heap[index]
            old_priority = pair[0]
            self.heap[index] = (old_priority, key)
            self._sift_down(index)
            self.pop()

    def get_priority(self, str key):
        if self.contains(key):
            index = self.key_index[key]
            priority = self.heap[index][0]
            return priority
        else:
            return None 

    def is_empty(self):
        return len(self.heap) == 0