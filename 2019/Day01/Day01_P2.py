import math

def FuelReqForModule(ModuleFuel):
    total_mod_fuel = 0
    while ModuleFuel > 0:
        total_mod_fuel += ModuleFuel
        ModuleFuel = ( math.floor( int(ModuleFuel) / 3 ) - 2 )   
    return int(total_mod_fuel)

fuel_req = 0
total_spacecraft_fuel = 0
with open("Day01/input.txt") as f:
    for ModuleMass in f:
       Fuel_req = ( math.floor( int(ModuleMass) / 3 ) - 2 )
       total_mod_fuel = FuelReqForModule(Fuel_req)
       total_spacecraft_fuel += total_mod_fuel
    
print("Total fuel needed : ", total_spacecraft_fuel)