# Functions output a Boolean list if password is valid

def PasswordPhilosphy( arr ):
    # List comprehension to check if the number of a certain letter appears more than x and less than y
    output = [ 
        True 
        if int(numRange.split("-")[0]) <= passwd.count( letter[0] ) <= int(numRange.split("-")[1]) 
        else False 
        for numRange, letter, passwd in arr 
    ]
    return output

def PasswordPhilosphyPart2( arr ):
    # List comprehension to check if the number of a certain letter only appears 1 in either location but not both
    # Is suggested that the passwd string starts with the index of 1
    output = [ 
        True
        if (passwd[ int( numRange.split("-")[0] ) - 1] == letter[0] or passwd[ int( numRange.split("-")[1] ) - 1] == letter[0]) 
            and passwd[ int( numRange.split("-")[0] ) - 1] != passwd[ int( numRange.split("-")[1] ) - 1] 
        else False 
        for numRange, letter, passwd in arr 
    ]
    return output

def PasswordPhilosphyPart2NoLC( arr ):
    output = []
    for numRange, letter, passwd in arr:
        minRange, maxRange = map(int, numRange.split("-"))
        letter = letter[0]

        if ( passwd[minRange - 1] == letter or passwd[maxRange - 1] == letter ) and passwd[minRange - 1] != passwd[maxRange - 1]:
            output.append( True )
        else:
            output.append( False )

    return output

with open("Day02/input.txt") as f:
    arr = [line.split() for line in f]

result = sum( PasswordPhilosphy( arr ))
print(f"Part 1 : {result}" )
resultPart2 = sum( PasswordPhilosphyPart2( arr ) )
print(f"Part 2 : {resultPart2}" )
resultPart2 = sum( PasswordPhilosphyPart2NoLC( arr ) )
print(f"Part 2 No List Comp : {resultPart2}" )