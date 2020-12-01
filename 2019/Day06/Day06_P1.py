UOM_Arr = []
links = []

def check(planet):
    for y in range( len(links) ):
        if links[y][0] == planet:
            return True

def Add_to_links(x, orbits):
    content = (x, orbits)
    links.append(content)

def iteration(x, numOrbitsToCOM, origin):
    if UOM_Arr[x][0] == "COM":
        Add_to_links(origin, numOrbitsToCOM)
    else:
        for y in range(len(UOM_Arr)):
            if UOM_Arr[y][1] == UOM_Arr[x][0]:
                if check(UOM_Arr[y][1]):
                    Add_to_links(origin, links[y][1] + numOrbitsToCOM)
                else:
                    iteration(y, numOrbitsToCOM + 1, origin)

def Calculate_Total_Orbits():
    counter = 0
    for z in range( len(links)):
        counter += links[z][1]
    return counter

with open("Day06/input2.txt") as f:
    for line in f:
        UOM_Arr.append(line.strip().split(")"))

x = 0
while x != len(UOM_Arr):
    iteration(x, 1, UOM_Arr[x][1])
    x += 1

print("Total orbits : ", Calculate_Total_Orbits() )