import os, re

# Part 1
def getNumOfMatches( card ):
    x = card[card.find(':')+1:]
    y = x.split('|')
    winning_numbers = set(list(map( int, y[0].split())))
    my_numbers = set(list(map( int, (y[1].split()))))
    matches =  winning_numbers.intersection( my_numbers )
    return len(matches)

def FunctionName( data ):
    points = 0
    for card in data:
        numOfMatches = getNumOfMatches( card )
        points += 2**(numOfMatches - 1) if( numOfMatches > 0 ) else 0
    return points

# Part 2

def FunctionName2( data ):
    scratchcards = [ 1 for i in data ]
    for i, card in enumerate(data):
        numOfMatches = getNumOfMatches( card )
        for x in range( 1, numOfMatches + 1 ):
            scratchcards[i+x] += (1 * scratchcards[i])

    return sum( scratchcards )


with open(f'{os.path.splitext(os.path.basename(__file__))[0]}/input.txt') as f:
    data = [ line.strip() for line in f]

p1Answer = FunctionName( data )
p2Answer = FunctionName2( data )

print()
print(f'Part 1: : {p1Answer}')
print(f'Part 2: : {p2Answer}')
print()