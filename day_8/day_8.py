import numpy as  np

from collections import defaultdict


f = open('day_08.txt')


arr = [int(x) for x in open('day_08.txt').read().strip()]

n_layers = len(arr)/(25*6)

print(n_layers)

d = defaultdict(lambda :defaultdict(int))

maximum = 0

# c = defaultdict(lambda : defaultdict(int))

for l in range(int(n_layers)):
    for i in range(25*6):
        # if ( arr[l*25*6 + i] == 0):
            d[l][arr[l*25*6 + i]] += 1






minimum = 10000
for l in range(int(n_layers)):
    if (d[l][0]<= minimum):
        minimum = d[l][0]
        saved_l = l

## layer number 
# b = maximum[1]

b = saved_l

## part_1 answer
print(d[b][1] * d[b][2])

#print(b)


