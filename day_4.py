# c = 0;
# for i in range(108457,562042):
#     a= str(i)
#     for x in range(len(a)-1):
#         if (a[x]<=a[x+1]):
#             if (a[x]==a[x+1]):
#                 c+=1



def count_letters(word):
    local = dict()
    w_set =set(word)
    local = {val:0 for val in w_set}
    for i in range(len(word)-1):
      if (word[i] == word[i+1]):
        local[word[i]]+=1
    return local





n=0



for i in range(171309,643603):
    d = dict() 
    c1,c2 = 0 ,0
    a = str(i)
    d = count_letters(a)
    for x in range(len(a)-1):


      if (int(a[x]) <= int(a[x+1])):
          c1+=1        
          if (a[x]==a[x+1]):
                c2+=1            
      if (c1==5 and c2>0):
          if 1 in d.values():
                n+=1



print(n)

