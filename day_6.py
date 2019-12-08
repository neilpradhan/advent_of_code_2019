from typing import NamedTuple, List , Dict


# import pytest

# from support import timing


f = open('day_06.txt')

class Node(NamedTuple):
    baap : str
    beta :str

    @staticmethod
    def constructor_string(s:str)->"Node":
        baap, beta  = s.strip().split(")")
        return Node(baap,beta)


def dictionary_of_betas(Nodes:List[Node])->Dict[str,str]:
    d = {}
    for baap, beta in Nodes:
        d[beta] = baap
    return d

## we have a dictionary of parents of every child and we need to calculate all posible generations of a child

def calculate_all_baaps(beta : str,d:Dict[str,str])->int:
    i=0
    while (beta != "COM"):
        i+=1
        beta  = d[beta]
    return  i






## we will make list of Nodes first through static method

# for line in f :
    # Node.constructor_string(line)

NODELIST = [Node.constructor_string(line) for line in f]




# print(NODELIST)

d = dictionary_of_betas(NODELIST)

counter  = 0
for beta in d:
    counter+=calculate_all_baaps(beta, d)
print("counter",counter) # ans1 cleared


def path_to_root(beta : str,d : Dict[str,str])-> List[str]:
    path = [beta]
    while (beta != "COM"):
        beta =d[beta]
        path.append(beta)
    return path


## Sam aur apna Baap ke beech ka min distance nikalna hai
## shortest path will be intersection of two paths


def minimum_path (beta1 :str , beta2 : str, d: Dict[str,str])-> int:
    path_1 = path_to_root(beta1,d)
    path_2 = path_to_root(beta2,d)

    while path_1 and path_2 and path_1[-1]==path_2[-1]:
        
        path_1.pop()
        path_2.pop()
    # print(path_1, path_2)
    return len(path_1) +  len(path_2) 






l = minimum_path(d["YOU"], d["SAN"], d)
print(l)



