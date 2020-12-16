def TicketTranslation( rd , ntickets ):
    # eR - error rate array, rd - rule dictionary , ntickets - nearby tickets
    # if valid sums the number of rules that v can be applyed
    # if valid == 0 that number is an error

    eR = []

    for ticket in ntickets:
        for v in ticket:
            valid = sum( [ rd[key]( int(v) ) for key in rd.keys() ] )
            if valid == 0:
                eR.append(int(v))       

    return sum(eR)

def TicketTranslationP2():
    # Finds all tickets that have an invalid number and removes them from the list
    invalid = []

    for i, ticket in enumerate(ntickets):
        for v in ticket:
            valid = sum( [ rd[key]( int(v) ) for key in rd.keys() ] )
            if valid == 0:
                invalid.append(i)
                break

    invalid.sort(reverse=True)

    for x in range(0, len(invalid) ):
        ntickets.pop( invalid[x] )

    # ----------------------------------------------------------------------------

    # Finds every field that every ticket is valid for, then appends then to a list
    # pfield : possible fields { where every ticket the value meets the rules }

    numOfTickets = len(ntickets)
    pfield = []
    
    for key in rd.keys():
        for f in range(0 , len(ntickets[0]) ):
            
            valid = sum( [ rd[key](int(ticket[f])) for ticket in ntickets ] )
            
            if valid == numOfTickets:
                pfield.append( (key , f) )

    # ----------------------------------------------------------------------------

    # Searches the list from above for which fields can be which and returns a dictionary of fields

    fields = {}
    keys = list(rd.keys())

    while fields.keys() != rd.keys():
        for key in keys:
            if sum(x.count(key) for x in pfield) == 1:
                ind = [ i for i, value in enumerate(pfield) if value[0] == key ]
                x = pfield[ ind[0] ][1]
                fields[ key ] = x
                pfield = [ (field,value) for field , value in pfield if value != x ]
                keys.pop( keys.index(key) )

    # ----------------------------------------------------------------------------

    # Calculates the 6 fields that have the keyword "Departure"

    answer = 1

    for key in keywordArr:
        print( key, fields[key] )
        answer *= int(mticket[0][ fields[key] ])

    return answer

def createRuleDictionary():
    # https://www.programiz.com/python-programming/methods/built-in/eval
    # Requires eval to create dyanamic, because r is a variable which has different value for each iteration of the loop. 
    # But when you do lambda x: r[0] <= x <= r[1], it does not use value of number. 
    # It just creates a lambda method that will use value of number when it will be called/used. So when you use you methods, 
    # r has the same values as the last loop which is used in every call to rd[ field ]( v )
    
    # rd[ field ] = lambda x : r[0] <= x <= r[1] or r[2] <= x <= r[3]
    # rd[ field ] = lambda x : 1 <= x <= 3 or 5 <= x <= 7


    for field, rule in rules:
        r = list(map(int, rule.replace(" or ", "-").split("-")))
        rd[ field ] = eval( f'lambda x : {r[0]} <= x <= {r[1]} or {r[2]} <= x <= {r[3]}' )
        if keyword in field:
            keywordArr.append( field )

# Main

filename = "Day16/input.txt"
arr = [ content.split("\n") for content in open( filename ).read().split("\n\n")]

keyword = "departure"
keywordArr = []

rules = [ line.split(": ") for line in arr[0] ]
rd = {}
createRuleDictionary()

mticket = [ values.split(",") for values in arr[1][1:] ]
ntickets = [ values.split(",") for values in arr[2][1:] ]

print( f'Part 1 answer : {TicketTranslation( rd , ntickets )}')
print( f'Part 2 answer : {TicketTranslationP2( )}')