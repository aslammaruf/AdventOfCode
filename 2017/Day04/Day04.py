
result = 0

def passphrase( line ):
    # Part 2 Addition, loops through every word in arr and rearranges by letter
    for x in range( len(line) ):
       line[x] = sorted(line[x])
    
    # from stackoverflow
    # line = ["".join(sorted(x)) for x in line]
    
    # End Part 2

    check = True
    for word in line:
        if line.count(word) > 1: # if more than 1 occurance of the word, passphrase fails
            check = False
            break

    return check
    
# Main Code

with open("Day4_input.txt") as f:
    for line in f:
        result += 1 if passphrase( line.split() ) else 0

print(result)