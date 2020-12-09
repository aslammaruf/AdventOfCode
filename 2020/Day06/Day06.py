def CustomCustoms( arr ):
    # Converts group into a list of letters, then converts list into set to remove all duplicates
    return sum([ len( set( "".join( group )) ) for group in arr ])

def CustomCustomsP2( arr ):
    # For each Group, creates a list of letters and the number of people in each group
    # Checks every different letter from the list if equal to number of people than add to new list
    count = 0
    for i, group in enumerate(arr):
        group = list("".join(group))
        lenGroup = len( arr[i] )
        count += len([ letter for letter in set(group) if group.count( letter ) == lenGroup ])
    return count

# Main

filename = 'Day06/input.txt'
arr = [ line.split('\n') for line in open( filename ).read().split('\n\n')]

print(f'Part 1 result : {CustomCustoms( arr )}')
print(f'Part 2 result : {CustomCustomsP2( arr )}')