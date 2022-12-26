# originally scaffolded with chatgpt, then edited 

import heapq

cdef class PriorityQueue:
    cdef list heap
    cdef dict lookup

    def __init__(self):
        self.heap = []
        self.lookup = {}

    def push(self, str key, int priority, object element):
        heapq.heappush(self.heap, (priority, (key,element)))
        self.lookup[key] = element

    def pop(self):
        pair = heapq.heappop(self.heap)[1]
        del self.lookup[pair[0]]
        return pair[1]

    def contains(self, str key):
        return key in self.lookup

# do I need priority? definitely need remove
    def get(self, str key):
        return self.lookup[key][1]

    def remove(self,str key):
        # NEED TO GET RID OF PQ side too

        del self.lookup[key]

# ignore resetting priority atm, can just remove and readd if I want
    # def set_priority(self, str key, int priority):
    #     element = self.lookup[key]
    #     index = self.heap.index((self.heap[index][0], element))
    #     self.heap[index] = (priority, element)
    #     heapq.heapify(self.heap)
