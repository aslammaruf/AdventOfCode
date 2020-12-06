filename = 'Day06/input.txt'
arr = [ line.split('\n') for line in open( filename ).read().split('\n\n')]

def CustomCustoms( arr ):
    # Converts group into a list of letters, then converts list into set to remove all duplicates
    return sum([ len( set("".join( group )) ) for group in arr ])

def CustomCustomsP2( arr ):
    # Creates a new set containing every letter thats appears in for all people in group
    # Then sums up the lens of each group, TEST print( arr[0], *arr[0], set(arr[0][0]), sep="\n")
    return sum( [ len( set( group[0] ).intersection( *group ) ) for group in arr ] )

print(f'Part 1 result : {CustomCustoms( arr )}')
print(f'Part 2 result : {CustomCustomsP2( arr )}')