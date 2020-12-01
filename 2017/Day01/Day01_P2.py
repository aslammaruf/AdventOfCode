
def InverseCaptcha( text ):
    text = text.strip()
    result = 0

    matchdistance = int(len(text) / 2)

    for x in range( matchdistance ):

        if ( x < matchdistance and text[x] == text[x + matchdistance]):
            result += int( text[x] ) * 2

    return result
    

with open("Day1_input.txt") as f:
    for line in f:
        result = InverseCaptcha( line )
        print( result )

