def main():
    filename = 'Day05/input.txt'
    arr = [ line for line in open( filename ).read().split('\n')]

    p1Result , p2Result = BinaryBoarding( arr )

    print( f'Part 1 result, Highest SeatID is : {p1Result}')
    print( f'Part 2 result, Found your seat at : {p2Result}')

def BinaryBoarding( arr ):
    # Creates list of Seat IDs using the equation = row * 8 + col 
    seatIDs = [ getLoc( boardingPass[:-3] , 128 ) * 8 + getLoc( boardingPass[-3:] , 8 ) for boardingPass in arr ]  
    return max( seatIDs ), *getSeat( seatIDs )

def getLoc( data, uBound ):
    loc = 0

    for x in data:
        diff = ( uBound - loc )/ 2
        if x == "F" or x == "L":
            uBound -= diff
        else:
            loc += diff

    return int(loc)

def getSeat( seatIDs ):
    return list(set( [ x for x in range( min(seatIDs) , max(seatIDs)) ] ).difference(set( seatIDs )) )

if __name__ == "__main__":
    main()