passwd_len = 6
accept_passwd = []

def Check1():
    for x in range(passwd_len - 1):
        if int(passwd_arr[x]) > int( passwd_arr[x + 1]):
            break
        elif x == passwd_len - 2:
           return True

def Check2():
    for x in range(passwd_len - 1):
        if int(passwd_arr[x]) == int( passwd_arr[x + 1]):
            return True

for passwd in range(372304,847060):
    passwd_arr = list(str(passwd))
    decreasingValue = Check1()
    doubleValue = Check2()
    if decreasingValue == True and doubleValue == True:
        accept_passwd.append(passwd)


print("Number of Acceptable Passwd : ", len(accept_passwd))