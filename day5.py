import numpy as np
from  typing import  List, NamedTuple, Tuple
f = open('day_05.txt')

def get_modes(instruction: int)-> Tuple[int, List[int]]:
    op = instruction % 100
    hund = (instruction // 100) % 10  
    thousand = (instruction // 1000) %10 
    ten_thousand = (instruction //10000) % 10
    return op,[hund, thousand, ten_thousand]


array = []
for line in f: # read rest of lines
    array.append([int(x) for x in line.split(",")])

arr = array[0]

# print(arr[0])

## only two modes possible 0 or 1 

def solve_problem (arr :List[int] , input : List[int] )-> List[int]:
    i = 0
    output = []
    # make a local array as we want output this time and dont want to change the array unnecessarily
    arr = arr[:]

    while arr[i]!=99:
        op = arr[i]
        op, modes  = get_modes(op)
        print(i,op,modes)
        if op == 1:
            if modes[0] == 0:
                v_1 = arr[arr[i+1]] 
                #print(f"loc1 is{arr[i+1]} and value is {v_1}")
            else: # if mode is 1
                v_1 = arr[i+1]
                #print(f"first value is {v_1}")
            # similarly for mode[1]
            if modes[1] == 0:
                v_2 = arr[arr[i+2]]
            else : # mode is 1
                v_2 = arr[i+2]
            arr[arr[i+3]] = v_1 + v_2
            i+=4            

        elif op == 2:
            if modes[0] == 0:
                v_1 = arr[arr[i+1]] 
                #print(f"loc1 is{arr[i+1]} and value is {v_1}")
            else: # if mode is 1
                v_1 = arr[i+1]
            # similarly for mode[1]
            if modes[1] == 0:
                v_2 = arr[arr[i+2]]
            else: # mode is 1
                v_2 = arr[i+2] 
            arr[arr[i+3]] = v_1 * v_2
            i+=4
        elif  op == 3:

            taking_loc  = arr[i+1]
            # (x,y) take x and store in location y
            taking_ip = input[0]
            # storing in y
            input = input[1:]
            arr[taking_loc] = taking_ip
            ## now input will change
            i+=2
            print(f"i is {i}")
        
        elif op == 4:
            # output at address 50 
            given_val =  arr[i+1]
            if modes[0] == 0:
                x = arr[arr[i+1]]
                output.append(x)
            else:
                output.append(given_val)
            i+=2
        elif op==5:
            if modes[0] == 0:
                v_1 = arr[arr[i+1]] 
                #print(f"loc1 is{arr[i+1]} and value is {v_1}")
            else: # if mode is 1
                v_1 = arr[i+1]
                #print(f"first value is {v_1}")
            # similarly for mode[1]
            if modes[1] == 0:
                v_2 = arr[arr[i+2]]
            else : # mode is 1
                v_2 = arr[i+2]
            if (v_1 !=0):
                i =v_2
            else:
                i+=3
        elif op == 6:
            if modes[0] == 0:
                v_1 = arr[arr[i+1]] 
                #print(f"loc1 is{arr[i+1]} and value is {v_1}")
            else: # if mode is 1
                v_1 = arr[i+1]
                #print(f"first value is {v_1}")
            # similarly for mode[1]
            if modes[1] == 0:
                v_2 = arr[arr[i+2]]
            else : # mode is 1
                v_2 = arr[i+2]
            if (v_1 ==0):
                i = v_2
            else:
                i+=3
                
        elif op == 7:
            if modes[0] == 0:
                v_1 = arr[arr[i+1]] 
                #print(f"loc1 is{arr[i+1]} and value is {v_1}")
            else: # if mode is 1
                v_1 = arr[i+1]
                #print(f"first value is {v_1}")
            # similarly for mode[1]
            if modes[1] == 0:
                v_2 = arr[arr[i+2]]
            else : # mode is 1
                v_2 = arr[i+2]
            if (v_1 <v_2):
                arr[arr[i+3]] = 1
            else:
                arr[arr[i+3]] = 0                
            i+=4

        elif op == 8:
            if modes[0] == 0:
                v_1 = arr[arr[i+1]] 
                #print(f"loc1 is{arr[i+1]} and value is {v_1}")
            else: # if mode is 1
                v_1 = arr[i+1]
                #print(f"first value is {v_1}")
            # similarly for mode[1]
            if modes[1] == 0:
                v_2 = arr[arr[i+2]]
            else : # mode is 1
                v_2 = arr[i+2]
            if (v_1 == v_2):
                arr[arr[i+3]] = 1
            else:
                arr[arr[i+3]] = 0   

            i+=4
        else:
            raise RuntimeError(f"invalid opcode: {arr[i],i}")
    return output




# ans1 = solve_problem(arr,[1])


# print(ans1)

#print(arr)

test_input_1 = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
test_input_2 = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]


#ans1 = solve_problem(arr,[1])

# ans_test = solve_problem()


ans_test_2 = solve_problem(arr,[5])
print(ans_test_2)