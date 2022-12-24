# idea: a queue where you take things of soonest event for things to happen
# might be worth switching to rust if structs become fun
# state changes always need to occur before decisions

import queue.PriorityQueue as pq

# we can put order as negative time, so earlier elements have earlier priority
# maybe no need for this combined wrapper
class event:
    def __init__(self,time,stateChange,decision):
        self.time = time;
        self.stateChange = stateChange;
        self.decision = decision;

# a tag search for a given element, then just apply the change to it 
class stateChange:
    def __init__(tag,change):
        self.tag = tag;
        self.change = change;
    def apply(self,overall_state):
        for element in overall_state:
            if element.tag == self.tag:
                # need to verify pass by reference
                element = change(element)
