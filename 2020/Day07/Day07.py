filename = "Day07/input.txt"
arr = [ line.strip(" .").split(" contain ") for line in open( filename ).read().split("\n")]

def HandyHaversacks( arr ):
    openList = ["shiny gold bag"]
    closedList = []

    while openList:
        # Creates list of every bag that can contain the item in openList[0] and that is not already been found
        # bag[:-1] used to remove the s at end of bags
        x = [ bag[:-1] for bag, contains in arr if openList[0] in contains and bag[:-1] not in closedList ] 
        # Adds 
        closedList.extend( x )
        openList.extend( x )
        openList.pop( 0 )

    return len(closedList)

def HandyHaversacksP2( searchStr ):
    # Recursive Method
    count = 0 

    x = [ contains.split(", ") for bag, contains in arr if searchStr in bag ]
    if x:
        for bag in x[0]:
            bag = bag.split(" ", 1)
            numOfbags = 0 if bag[0] == "no" else int(bag[0])
            count += numOfbags + numOfbags * HandyHaversacksP2( bag[1] )

    return count

print( f'Part 1 answer : {HandyHaversacks( arr )}')
print( f'Part 2 answer : {HandyHaversacksP2( "shiny gold bag" )}')