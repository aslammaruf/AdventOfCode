UOM_Arr = []
links  = []

def check(planet):
    for y in range( len(links) ):
        if links[y][0] == planet:
            return True

def Add_to_links(x, orbits):
    content = (x, orbits)
    links.append(content)

def iteration(x, numOrbitsToCOM, origin):
    currentPlanet = UOM_Arr[x][1]
    if UOM_Arr[x][0] == "COM":
        Add_to_links(currentPlanet, numOrbitsToCOM) 
    else:
        for y in range(len(UOM_Arr)):
            if UOM_Arr[y][1] == UOM_Arr[x][0]:
                if check(UOM_Arr[y][1]):
                    Add_to_links(currentPlanet, numOrbitsToCOM)
                else:
                    iteration(y, numOrbitsToCOM + 1, origin)
                    Add_to_links(currentPlanet, numOrbitsToCOM)

def Calculate_Total_Orbits():
    counter = 0
    for z in range( len(links)):
        counter += links[z][1]
    return counter

with open("Day06/input.txt") as f:
    for line in f:
        UOM_Arr.append(line.strip().split(")"))

x = 0
while x != len(UOM_Arr):
    links = []
    if UOM_Arr[x][1] == "SAN":
        iteration(x, -1, UOM_Arr[x][1])
        Array_1 = links.copy()
    if UOM_Arr[x][1] == "YOU":
        iteration(x, -1, UOM_Arr[x][1])
        Array_2 = links.copy()
    x += 1

ComparedArray = []
for i in range( len(Array_1) ):
    for j in range( len(Array_2) ):
        if Array_1[i][0] == Array_2[j][0]:
            contents = (Array_1[i][0], Array_1[i][1], Array_2[j][1])
            ComparedArray.append(contents)

shortestJumps_line = ComparedArray[-1]
shortestJumps = shortestJumps_line[1] + shortestJumps_line[2]
print(shortestJumps)
print("Total orbits : ", Calculate_Total_Orbits() )