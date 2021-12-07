# Part 1

def GiantSquid( arr ):
    boardarr = arr[2:]
    boards = []

    for x in range(0, len(boardarr), 6):
        temp = list(map( str.split , boardarr[ x : x + 5]))
        boards.append( temp )

    winner = False

    for num in arr[0].split(','):
        for board in boards:
            for row in board:
                if num in row: 
                    row[row.index( num)] = 'F'
                    winner = CheckWinner( board )
                if winner == True:
                    unmarked = 0
                    for i in board:
                        for j in i:
                            if j != "F" : unmarked += int(j)
                    ans = unmarked * int(num)
                    return ans

    return 'Answer Not Found'

# Part 2

def GiantSquidP2( arr ):
    boardarr = arr[2:]
    boards = []

    for x in range(0, len(boardarr), 6):
        temp = list(map( str.split , boardarr[ x : x + 5]))
        boards.append( temp )

    winner = False
    winArr = []

    for num in arr[0].split(','):
        for idx, board in enumerate(boards):
            if idx not in winArr:
                for row in board:
                    if num in row:
                        row[row.index( num )] = 'F'
                        winner = CheckWinner( board )
                    if winner == True:
                        if len(winArr) < len(boards) - 1: 
                            winArr.append(idx)
                            winner = False
                        else:
                            unmarked = 0
                            for i in board:
                                for j in i:
                                    if j != "F" : unmarked += int(j)
                            ans = unmarked * int(num)
                            return ans

    return 'Answer Not Found'

def PrintBingoGrid( arr ):
    for x in arr:
        print(x)
    print('\n')

def CheckWinner( board ):
    winner = False

    # Check row
    for row in board:
        if row.count('F') == 5 : 
            winner = True
            break
    # Check column
    for i in range(0, len(board)):
        Found = 0
        for row in board:
            if row[i] == "F" : Found += 1
        if Found == 5 : 
            winner = True 
            break

    return winner


with open('Day04/input.txt') as f:
    arr = [ line.strip('\n') for line in f]

p1Answer = GiantSquid( arr )
p2Answer = GiantSquidP2( arr )

print()
print(f'Part 1: Bingo : {p1Answer}')
print(f'Part 2: Last Winning Bingo : {p2Answer}')
print()
