# Part 1

def SevenSegmentSearch( data ):
    total = 0
    for signal in data:
        output = signal[-4:]
        segNum = [ len(seg) for seg in output ]
        total += sum(map( segNum.count, [2, 4, 3, 7]))

    return total

# Part 2

def SevenSegmentSearchP2( data ):
    count = 0
    for signal in data:
        digits = [ 0 ] * 10
        
        segNum = [ len(seg) for seg in signal ]

        segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6 ]
        for x in range( 0, 10 ):
            digits[x] = list(set([ ''.join(sorted(list(y))) for idx, y in enumerate(signal) if segNum[idx] == segments[x]]))

        digits[9] = [ pos for pos in digits[9] if len( list( set(list(pos)) - set(list(digits[4][0])) )) == 2 ]
        digits[0] = [ pos for pos in digits[0] if len( list( set(list(pos)) - set(list(digits[7][0])) )) == 3 and pos not in digits[9] ]
        digits[6] = [ pos for pos in digits[6] if pos not in digits[9] and pos not in digits[0] ]

        digits[3] = [ pos for pos in digits[3] if len( list( set(list(pos)) - set(list(digits[7][0])) )) == 2 ]
        digits[5] = [ pos for pos in digits[5] if len( list( set(list(digits[9][0])) - set(list(pos)))) == 1 and pos not in digits[3] ]
        digits[2] = [ pos for pos in digits[2] if pos not in digits[3] and pos not in digits[5] ]

        output = [ ''.join(sorted(list(out))) for out in signal[-4:] ]

        for x, num in enumerate(output):
            output[x] = [ idx for idx, digit in enumerate(digits) if digit[0] == num ][0]

        count += int(''.join(list(map( str, output ))) )

    
    return count

with open('Day08/input.txt') as f:
    data = [ line.strip().split() for line in f]

p1Answer = SevenSegmentSearch( data )
p2Answer = SevenSegmentSearchP2( data )

print()
print(f'Part 1: : {p1Answer}')
print(f'Part 2: : {p2Answer}')
print()