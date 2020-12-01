
def TwistyTrampolines( arr, arr_len ):
    steps, counter = 0, 0 

    #print(f'Arr Len : {arr_len}')

    while counter <= arr_len - 1:
        steps += 1
        temp = counter

        counter += arr[counter]
        arr[temp] += -1 if counter - temp > 2 else 1


        #print(f'{arr}, current counter : {counter}')

    return steps


with open("Day5_input.txt") as f:
    arr = [int(x) for x in f]
    arr_len = len(arr)

    #print(f'Inital Arr : {arr}')
    result = TwistyTrampolines( arr , arr_len)

print(result)