def main():
    filename = 'Day04/input.txt'
    arr = [ line.replace('\n', ' ').split(' ') for line in open( filename ).read().split("\n\n") ]

    answer = PassportProcessing( arr )
    print( f'Part 2 Result : {answer}')

def checkInt( data , base = 10 ):
    try:
        int( data , base)
        return True
    except:
        return False

def checkHeight( data ):
    try:
        measurement = data[-2:]
        height = int(data[:-2])

        if measurement == "cm" and 150 <= height <= 193 or measurement == "in" and 59 <= height <= 76:
            return True
        else:
            return False
    except:
        return False

def PassportProcessing( arr ):
    validCheck = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    validCheck.sort()
    validCheck.remove('cid')
    eyeColours = [ 'amb' , 'blu' , 'brn' , 'gry' , 'grn' , 'hzl' , 'oth']

    valid = 0

    for passport in arr:
        currentpassport = []

        for i in passport:
            field = i[:3]
            data = i[4:]

            if field != 'cid':
                if field == 'byr' and 1920 <= int(data) <= 2002:
                    currentpassport.append( field )
                elif field == 'iyr' and 2010 <= int(data) <= 2020:
                    currentpassport.append( field )
                elif field == 'eyr' and 2020 <= int(data) <= 2030:
                    currentpassport.append( field )
                elif field == 'hgt' and checkHeight( data ):
                    currentpassport.append( field )
                elif field == 'hcl' and data[0] == '#' and checkInt( data[1:], 16 ):
                    currentpassport.append( field )
                elif field == 'ecl' and data in eyeColours:
                    currentpassport.append( field )
                elif field == 'pid' and len(data) == 9 and checkInt( data ):
                    currentpassport.append( field )


        currentpassport.sort()

        if currentpassport == validCheck:
            valid += 1
    
    return valid

if __name__ == "__main__":
    main()