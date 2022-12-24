#might change OOP format, could just be enum or something
class Buildable:
    def __init__(self,name,build_time,supply,mineralCost, gasCost):
        self.name = name
        #production relevant stats
        self.build_time = build_time
        self.supply = supply
        self.mineralCost = mineralCost
        self.gasCost = gasCost

class Structure(Buildable):
    def __init__(self,name,build_time,mineralCost, gasCost,upgrades=[]):
        #structures have no supply
        super().__init__(name,build_time,0,mineralCost, gasCost)
        self.upgrades = upgrades

class Unit(Buildable):
    def __init__(self,name,build_time,supply,mineralCost, gasCost,health=0,damage=0):
        super().__init__(name,build_time,supply,mineralCost, gasCost)
        self.health = health
        self.damage = damage