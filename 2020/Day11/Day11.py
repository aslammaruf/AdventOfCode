import copy
# Using copy.deepcopy() to create a copy of the arr as slicing was still changing both arrs

def seatingSystem( arr ):
    # History stores the last iteration of the seating plan
    # Top Left, Top Middle, Top Right , Mid Left, Mid Right, Bot Left, Bot Mid, Bot Right
    checkArr = [ (-1,-1) , (-1,0) , (-1,1) , (0,-1) , (0,1) , (1,-1) , (1,0) , (1,1) ]
    history = []

    while history != arr:
        history = copy.deepcopy(arr)

        for row in range( len(arr) ):
            for col in range( len(arr[0]) ):
                checkList = []

                # Creates a list if the seats around are occupied or not
                for i, j in checkArr:
                    if row + i >= 0 and row + i < len(arr) and col + j >= 0 and col + j < len(arr[0]):
                        checkList.append( True if history[row + i][col + j] == "#" else False )

                if history[row][col] == "L" and sum(checkList) == 0:
                    arr[row][col] = "#"
                elif history[row][col] == "#" and sum(checkList) >= 4:
                    arr[row][col] = "L"

    return sum( x.count("#") for x in arr )

def seatingSystemP2( arr ):
    # Top Left, Top Middle, Top Right , Mid Left, Mid Right, Bot Left, Bot Mid, Bot Right
    checkArr = [ (-1,-1) , (-1,0) , (-1,1) , (0,-1) , (0,1) , (1,-1) , (1,0) , (1,1) ]
    history = []

    while history != arr:
        history = copy.deepcopy(arr)

        for row in range( len(arr) ):
            for col in range( len(arr[0]) ):
                checkList = []

                for i, check in enumerate(checkArr):
                    x, y = check
                    found = 0
                    
                    while 0 <= row + x < len(arr) and 0 <= col + y < len(arr[0]) and found == 0:
                        if history[row + x][col + y] == "#":
                            checkList.append( True )
                            found = 1
                        elif history[row + x][col + y] == "L":
                            checkList.append( False )
                            found = 1
                        x += checkArr[i][0]
                        y += checkArr[i][1]

                if history[row][col] == "L" and sum(checkList) == 0:
                    arr[row][col] = "#"
                elif history[row][col] == "#" and sum(checkList) >= 5:
                    arr[row][col] = "L"

    return sum( x.count("#") for x in arr )

# Main 

filename = "Day11/input.txt"
inputArr = [ list(line) for line in open( filename ).read().split("\n") ]

print( f'Part 1 answer: {seatingSystem( copy.deepcopy(inputArr) )}')
print( f'Part 2 answer: {seatingSystemP2( copy.deepcopy(inputArr) )}')