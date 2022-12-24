# figure out mining models for sc2 things

#ignore mules/gold for one second

#https://liquipedia.net/starcraft2/Resources

#in minerals/minute, assumes 8 patches(can make more customizable later)
def mineralsPerBaseRate(mineral_workers):
    # one worker on mineral patch = 55-60 minerals/minute(dist dependent)
    # two workers on mineral patch = 110-120 minerals/minute(dist dependent)
    # three workers on mineral patch = 143 minerals/minute(dist independent)

    # assume optimality of distribution
    if mineral_workers <= 16:
        return mineral_workers*55
    elif mineral_workers <= 24:
        soFar = 16*55
        remaining = mineral_workers - 16
        return soFar + remaining*(143-110) #diminished returns
    else:
        return 1140 #max basically

# can refactor, probably a shorter way to write
# gas/min
def gasPerBaseRate(gas_workers,gases):
    # 1 worker 61 gas/min
    # 2 workers 123 gas/min
    # 3 workers 163 gas/min
    if gases == 1:
        if gas_workers <=2:
            return gas_workers*61
        else:
            return 163
    elif gases == 2:
        if gas_workers <=4:
            return  gas_workers*61
        elif gas_workers < 6:
            soFar = 163
            remaining = gas_workers - 3
            return soFar + remaining*61
        else:
            return 163*2
        

