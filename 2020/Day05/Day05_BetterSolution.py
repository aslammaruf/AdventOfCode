def main():
    filename = 'Day05/input.txt'
    arr = [ line for line in open( filename ).read().split('\n')]

    p1Result , p2Result = BinaryBoarding( arr )

    print( f'Part 1 result, Highest SeatID is : {p1Result}')
    print( f'Part 2 result, Found your seat at : {p2Result}')

def BinaryBoarding( arr ):
    # Creates list of Seat IDs using the equation = row * 8 + col 
    seatIDs = [ getLoc( boardingPass[:-3] ) * 8 + getLoc( boardingPass[-3:]) for boardingPass in arr ]  
    return max( seatIDs ), *getSeat( seatIDs )

def getLoc( data ):
    # Replacing String into Binary 0 and 1, then converting to integer with a base of 2
    data = data.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    return int( data, base = 2 )

def getSeat( seatIDs ):
    # Creates a list of numbers that don't appear in the SeatID array
    return [ x for x in range( min(seatIDs) , max(seatIDs)) if x not in seatIDs ]

if __name__ == "__main__":
    main()