def EncodingError():
    # If using test.txt use x = 5 otherwise default is 25
    x = preamble = 25
    
    while x < len(arr):
        valid = [ num for num in arr[x - preamble:x] if arr[x] - num in arr[x - preamble:x] and arr[x] - num != num]
        if valid:
            x += 1
        else:
            break
    
    print( f"first result that isnt't valid {arr[x], valid}" )
    return arr[x], x

def EncodingErrorP2( invalidNum, ub ):
    # lb is the lower bound, ub is the upper bound
    lb = 0 
    searchArr = arr[:ub] # Shorten the arr to remove anything after where the invalid number is found
    history = []

    while sum( searchArr[lb : ub] ) != invalidNum:
        # Loops until sum of the arr is equal to the invalid number found from part 1
        # check the is greater or equal to the invalid number and changes the upperbound
        # if arr is in history then increase the lowerbound
        if sum( searchArr[lb : ub - 1] ) >= invalidNum and searchArr[lb : ub - 1] not in history:
            ub -= 1
        elif sum( searchArr[lb : ub + 1] ) <= invalidNum and searchArr[lb : ub + 1] not in history:
            ub += 1
        else:
            lb += 1

        history = searchArr[lb : ub]

    return min(searchArr[lb : ub]) + max(searchArr[lb : ub])

# Main 

filename = "Day09/input.txt"
arr = [ int(line) for line in open( filename ).read().split("\n")]

invalidNum, x = EncodingError()
print( f'Part 1 answer : {invalidNum}')
print( f'Part 2 answer : {EncodingErrorP2( invalidNum, x )}')

