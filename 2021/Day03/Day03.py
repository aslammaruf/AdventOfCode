# Part 1

def BinaryDiagnostic( arr ):
    gammaRate = ""

    for i in range(0, len(arr[0]) ):
        charArr = [ data[i] for data in arr ]
        gammaRate += '0' if charArr.count('0') > charArr.count('1') else '1'

    return int(gammaRate, base=2) * int( gammaRate.replace("1", "2").replace("0", "1").replace("2", "0"), base=2 )

# Part 2

def BinaryDiagnosticP2( arr ):
    mcvArr = arr 
    lcvArr = arr

    for i in range( 0, len( arr[0] )):
        if len(mcvArr) != 1:
            mcvCharArr = [ data[i] for data in mcvArr ]
            mcv = '0' if mcvCharArr.count('0') > mcvCharArr.count('1') else '1' 
            mcvArr = [ data for data in mcvArr if data[i] == mcv ]
        if len(lcvArr) != 1:
            lcvCharArr = [ data[i] for data in lcvArr ]
            lcv = '0' if lcvCharArr.count('0') <= lcvCharArr.count('1') else '1'
            lcvArr = [ data for data in lcvArr if data[i] == lcv ]
            
    return int(mcvArr[0], base=2) * int( lcvArr[0], base=2)


with open('Day03/input.txt') as f:
    arr = [ line.strip('\n') for line in f]

p1Answer = BinaryDiagnostic( arr )
p2Answer = BinaryDiagnosticP2( arr )

print()
print(f'Part 1: Power consumption : {p1Answer}')
print(f'Part 2: Life support rating : {p2Answer}')
print()
