# CHATGPT generated, edited and worked on by Ibrahim

# needs a lot more work to be done 
import heapq
import functools

#action class will map things f

# Define a class for each event that will be added to the queue
class Event:
    def __init__(self, time, name, action):
        self.time = time
        self.action = action
        self.name = name
    
    def __lt__(self, other):
        # Define comparison function for events based on time
        return self.time < other.time

# assume simple minerals atm, eventually split by bases and gas sat or something
def miningRate(numWorkers):
    return numWorkers*1



# Define the current state of the game
state = {
    "time": 0,
    "minerals": 50,
    "gas": 0,
    "supply": 10,
    "supply_used": 0,
    "structures": {"Nexus":1},
    "units": {"Probe":12},
    "inProgress":[]
}

# Define the list of available units and structures
units = { 
    "Probe": {"minerals": 50, "gas": 0, "supply": 1, "build_time": 12},
    "Zealot": {"minerals": 100, "gas": 0, "supply": 2, "build_time": 30},
    "Stalker": {"minerals": 125, "gas": 50, "supply": 2, "build_time": 35},
    "Sentry": {"minerals": 50, "gas": 100, "supply": 2, "build_time": 40},
    "Observer": {"minerals": 25, "gas": 75, "supply": 1, "build_time": 30},
    "Colossus": {"minerals": 300, "gas": 200, "supply": 6, "build_time": 90},
    "Immortal": {"minerals": 275, "gas": 100, "supply": 4, "build_time": 60}
}

structures ={ 
    "Pylon": {"minerals": 100, "gas": 0, "build_time": 18},
    "Gateway": {"minerals": 150, "gas": 0, "build_time": 65},
    "Robotics Facility": {"minerals": 200, "gas": 100, "build_time": 65},
    "Stargate": {"minerals": 150, "gas": 150,  "build_time": 60},
    "Templar Archives": {"minerals": 150, "gas": 200,  "build_time": 50},
    "Dark Shrine": {"minerals": 100, "gas": 250, "build_time": 100},
    "Robotics Bay": {"minerals": 200, "gas": 200, "build_time": 80}
}

# each event will be a function state -> state, neweEvents

def addUnit(state,unitName):
    state["units"][unitName] += 1
    return (state, [])

def addStructure(state,structureName):
    state["structures"][structureName] += 1
    return (state, [])

def buildUnit(state,unitName):
    minCost = units[unitName]["minerals"]
    gasCost = units[unitName]["gas"]
    supply = units[unitName]["supply"]
    state["minerals"] -= minCost
    state["gas"] -= gasCost
    state["supply_used"] += supply
    addEvent = Event(state["time"] + units[unitName]["build_time"], unitName+" finished", lambda state: addUnit(state,unitName))
    return (state,[addEvent])

def buildStructure(state,structureName):
    minCost = structures[structureName]["minerals"]
    gasCost = structures[structureName]["gas"]
    state["minerals"] -= minCost
    state["gas"] -= gasCost
    addEvent = Event(state["time"] + structures[structureName]["build_time"], structureName+" finished", lambda state: addStructure(state,structureName))
    return (state,[addEvent])

def printState(state):
    print(f"Time: {state['time']}")
    print(f"Minerals: {state['minerals']}")
    print(f"Gas: {state['gas']}")
    print(f"Supply: {state['supply_used']}/{state['supply']}")
    print(f"Structures: {state['structures']}")
    print(f"Units: {state['units']}")



#finished the physical event framework, still haven't added decision making framework

# Initialize the priority queue with the initial event
event_queue = []
# heapq.heappush(event_queue, Event(0, "Start game", lambda state:buildUnit(state,"Probe")))


# Loop until the queue is empty
while event_queue:
    # Get the next event from the queue
    current_event = heapq.heappop(event_queue)
    
    # Update the state based on the time passed since the last event
    diff = current_event.time - state["time"]
    state["time"] += diff

    state["minerals"] += diff * miningRate(state["units"]["Probe"])
    
    # TO DO - adding new events upon completion

    printState(state)
    print(f"Event {current_event.name} at time {state['time']}")
    print("\n")


    state,newEvents = current_event.action(state)
    for event in newEvents:
        heapq.heappush(event_queue, event)

    #special cases
    if current_event.name == "Pylon finished":
        state["supply"] += 8
    

    #decision making




    # Perform the action for the current event
    # if current_event.action == "Start game":
    #      print(f"Game start at time {state['time']}")   

    # elif current_event.action == "Build structure":
    #     # Choose the next available structure to build
    #     structure = None
    #     for s in structures:
    #         if s["name"] not in state["structures"]:
    #             structure = s
    #             break
    #     if structure:
    #         # Add the cost of the structure to the state
    #         state["minerals"] -= structure["minerals"]
    #         state["gas"] -= structure["gas"]
    #         state["supply_used"] += structure["supply"]
    #         # Add the structure to the list of structures
    #         state["structures"].append(structure["name"])
    #         # Schedule the next event to occur when the structure finishes building
    #         heapq.heappush(event_queue, Event(state["time"] + structure["build_time"], "Structure finished"))
    #     else:
    #         print(f"No more structures to build at time {state['time']}")
    # elif current_event.action == "Structure finished":
    #     print(f"Structure finished at time {state['time']}")
    #     # Add more events to the queue based on the criteria you provided
    #     heapq.heappush(event_queue, Event(state["time"], "Build structure"))
    #     heapq.heappush(event_queue, Event(state["time"], "Build unit"))
    # elif current_event.action == "Build unit":
    #     # Choose the next available unit to build
    #     unit = None
    #     for u in units:
    #         if u["name"] not in state["units"]:
    #             unit = u
    #             break
    #     if unit:
    #         # Add the cost of the unit to the state
    #         state["minerals"] -= unit["minerals"]
    #         state["gas"] -= unit["gas"]
    #         state["supply_used"] += unit["supply"]
    #         # Add the unit to the list of units
    #         state["units"].append(unit["name"])
    #         # Schedule the next event to occur when the unit finishes building
    #         heapq.heappush(event_queue, Event(state["time"] + unit["build_time"], "Unit finished"))
    #     else:
    #         print(f"No more units to build at time {state['time']}")
    # elif current_event.action == "Unit finished":
    #     print(f"Unit finished at time {state['time']}")
    #     # Add more events to the queue based on the criteria you provided
    #     heapq.heappush(event_queue, Event(state["time"], "Build unit"))


