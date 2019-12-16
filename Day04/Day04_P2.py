passwd_len = 6
accept_passwd = []

def Check1():
    for x in range(passwd_len - 1):
        if int(passwd_arr[x]) > int( passwd_arr[x + 1]):
            break
        elif x == passwd_len - 2:
           return Check2()

def Check2():
    for x in range(passwd_len - 1):
        if int(passwd_arr[x]) == int( passwd_arr[x + 1]):
            if x == passwd_len - 2:
                if int(passwd_arr[x]) != int(passwd_arr[x - 1]):
                    return True
            elif int(passwd_arr[x]) == int( passwd_arr[x + 2]) or int(passwd_arr[x]) == int( passwd_arr[x - 1]) :
                pass
            else:
                return True
                

for passwd in range(134792,675810):
    passwd_arr = list(str(passwd))
    decreasingValue = Check1()
    if decreasingValue == True:
        accept_passwd.append(passwd)

print("Number of Acceptable Passwd : ", len(accept_passwd))