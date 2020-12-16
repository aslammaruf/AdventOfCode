import math

def shuttleSearch():
    fb = [ ( math.ceil( ts / int(id) ) * int(id)  , int(id) ) for id in shuttleArr if id != "x" ]
    print( fb )
    return  min(fb)[1] * ( min(fb)[0] - ts )

def shuttleSearchP2():
    # Solved Mathmatically using Chinese Remainder Theorem


# Main

f = open( "Day13/input.txt" , "r")
ts = int( f.readline() )
shuttleArr = f.readline().split(",")

print(shuttleArr)

print( f'Part 1 answer : {shuttleSearch()}')
print( f'Part 2 answer : {shuttleSearchP2()}')