# written by chat gpt: Prompt
# write me a cython script to implement a data structure 
# that is a priority queue that also allows O(1) lookups of elements

import heapq

cdef class PriorityQueue:
    cdef public list heap
    cdef public dict lookup

    def __init__(self):
        self.heap = []
        self.lookup = {}

    cdef void _push_helper(self, int priority, object element):
        heapq.heappush(self.heap, (priority, element))
        self.lookup[element] = priority

    def push(self, int priority, object element):
        self._push_helper(priority, element)

    def pop(self):
        priority, element = heapq.heappop(self.heap)
        del self.lookup[element]
        return element

    def contains(self, object element):
        return element in self.lookup

    def get_priority(self, object element):
        return self.lookup[element]

    def set_priority(self, object element, int priority):
        del self.lookup[element]
        self._push_helper(priority, element)

