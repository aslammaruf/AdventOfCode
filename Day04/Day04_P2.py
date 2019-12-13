import math

passwd_len = 6
accept_passwd = []

def Check1(): # Checks digits don't decrease
    for x in range(passwd_len - 1):
        if int(passwd_arr[x]) > int( passwd_arr[x + 1]):
            break
        elif x == passwd_len - 2:
           return True

# Part 2 requires additional check
def Check2():
    for x in range(passwd_len - 1):
        if int(passwd_arr[x]) == int( passwd_arr[x + 1]): # Checks for doubles in number
            return True

def Check3():
    pass

#for passwd in range(372304,847060):
for passwd in range(111000,112000): 
    passwd_arr = list(str(passwd))
    decreasingValue = Check1()
    doubleValue = Check2()
    largerGroup = Check3()
    if decreasingValue == True and doubleValue == True and largerGroup == True:
        accept_passwd.append(passwd)

print(accept_passwd)
print("Number of Acceptable Passwd : ", len(accept_passwd))