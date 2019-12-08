import numpy as np
import re
f = open('day_03.txt')

# a,b  =  f.read().split("\n")


directions = {
    'L' : (-1,0),
    'R' : (1,0),
    'U' : (0,1),
    'D' : (0,-1),
 }




i = 0
array = [None]*2 
for line in f:
    array[i] = ([str(x) for x in line.split(",")])
    i+=1
## all are string
arr_1=array[0]
arr_2 = array[1]

#print(arr_1)

## this function will return tuples of (x,y) in a array
def return_points(arr_1: array)-> array:

    wire_len =  dict()
    points = set()
    x=0
    y=0
    l = 0
    for element in arr_1:
        dir , n = element[0] ,  int(element[1:])
        for _ in range(n):
            x+= directions[dir][0]
            y+= directions[dir][1]
            t=(x,y)
            l+=1
            if  (x,y) not in  wire_len:
                wire_len[(x,y)] = l

            points.add(t)
    return points, wire_len



A , lA =  return_points(arr_1)

B, lB =  return_points(arr_2)


## common points are intersection of two sets
intersection_set = A & B

ans_1 = min([abs(x) + abs(y) for x,y in intersection_set])

print(ans_1)



ans_2 = min([lA[k]+ lB[k] for k in intersection_set])



print(ans_2)