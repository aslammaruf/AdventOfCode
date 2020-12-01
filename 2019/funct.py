def readFile( path ):
    
    with open( path ) as f:
        output = [ line for line in f ]

    return output
