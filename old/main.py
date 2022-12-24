from zerg import Hatchery
from buildable import Unit
# might need to write callable wrappers for hatches

structureOptions = []
structureOptions.append(Hatchery)

unitOptions = []

unitOptions.append(Unit("Drone",12,1,50,0,40))

currentUnits = []
currentStructure = []
supply = 0
workers = 0
gasCount = 0
minerals = 0
gas = 0


# initial
currentStructure.append(Hatchery(0))
currentUnits = [Unit("Drone",12,1,50,0,40) for i in range(12)]
supply = 12

#let's optimize fastest way to 18 supply

while 
