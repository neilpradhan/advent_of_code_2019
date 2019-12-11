import numpy as  np

from collections import defaultdict

import numpy as np
import matplotlib.pyplot as plt



f = open('day_08.txt')


arr = [int(x) for x in open('day_08.txt').read().strip()]

n_layers = len(arr)/(25*6)

print(n_layers)

d = defaultdict(lambda :defaultdict(int))




for l in range(int(n_layers)):
    for i in range(25*6):
            d[l][arr[l*25*6 + i]] += 1






minimum = 10000
for l in range(int(n_layers)):
    if (d[l][0]<= minimum):
        minimum = d[l][0]
        saved_l = l

## layer number 
# b = maximum[1]

b = saved_l
print(d[b][1] * d[b][2])

print(b)



##3 part b


Final_array = [[' ' for _ in range(25)] for _ in range(6)]

for l in range(int(n_layers)):
    ## for every layer
    for row in range(6):
        for col in range(25):
            if (arr[l*25*6 + row*25 + col] == 0 and Final_array[row][col] == ' '):
                    Final_array[row][col] = '0'
            elif (arr[l*25*6 + row*25 + col] == 1 and Final_array[row][col] == ' '):
                    Final_array[row][col] = '1'



# plt.plot(Final_array)
# plt.show()


for row in range(6):
    for col in range(25):
        print(Final_array[row][col],end = ' ')
    
    print(end = "\n")