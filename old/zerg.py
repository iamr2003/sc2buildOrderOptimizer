# try to write out zerg specific things

from buildable import Structure

# larvae are generated every 11 seconds

class Hatchery(Structure):
    def __init__(self,time):
        upgrades = [] #eventually add in the burrow, ov speed
        super().__init__("Hatchery",71,300,0,upgrades)
        self.supply = 0
        self.larvae = 1 #spawns with 1 larvae iirc
        self.lastLarvaeTime = time
    def getLarvae(self,time): # fun async updates
        #ignoring injects initially
        if time - self.lastLarvaeTime >= 11:
            diff = time - self.lastLarvaeTime
            num = diff // 11
            remaining = diff % 11
            self.lastLarvaeTime = time - remaining
            self.larvae += num
        return self.larvae
    

