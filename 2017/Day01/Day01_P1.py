
def InverseCaptcha( text ):
    text = text.strip()
    result = 0

    for x in range( len(text) ):

        if ( x == len(text) - 1 and text[x] == text[0] ) or ( x < len(text) - 1 and text[x] == text[x + 1]):
            result += int( text[x] )

    return result
    

with open("Day1_input.txt") as f:
    for line in f:
        result = InverseCaptcha( line )
        print( result )

