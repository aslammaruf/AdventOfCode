# Part 1

def SyntaxScoring( data ):
    iChars = [ getCorrupted( subSystem, True ) for subSystem in data ]
    return ( iChars.count(')') * 3 ) + ( iChars.count(']') * 57 ) + ( iChars.count('}') * 1197 ) + ( iChars.count('>') * 25137 )

# Part 2

def SyntaxScoringP2( data ):
    data = [ subSystem for idx, subSystem in enumerate( data ) if getCorrupted( subSystem, True ) == 0 ]
    autoComplete = [ getCorrupted( subSystem, False ) for subSystem in data ]
    scores = sorted([ getScores(x) for x in autoComplete ])
    return scores[ int(((len(scores) + 1) / 2) - 1)] 

def getCorrupted( subSystem, r0 ):
    chunkOpen = []
    for chunk in subSystem:
        if chunk in cOpen:
            chunkOpen.append( cOpen.index( chunk ) )
        elif chunk in cClose:
            if cClose.index( chunk ) == chunkOpen[-1]:
                chunkOpen.pop(-1)
            else:
                return chunk

    return 0 if r0 == True else chunkOpen[::-1]

def getScores( autoComplete ):
    score = 0
    for chunk in autoComplete:
        score = ( score * 5 ) + ( chunk + 1 )
    return score

cOpen = [ '(', '[', '{', '<' ]
cClose = [ ')', ']', '}', '>' ]

with open('Day10/input.txt') as f:
    data = [ list(line.strip()) for line in f]

p1Answer = SyntaxScoring( data )
p2Answer = SyntaxScoringP2( data )

print()
print(f'Part 1: : {p1Answer}')
print(f'Part 2: : {p2Answer}')
print()