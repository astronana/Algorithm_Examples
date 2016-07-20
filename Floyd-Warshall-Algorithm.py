# Floyd-Warshall-Algorithm
# Path is a random n*n matrix where Path[i,j] represent the cost moving from i to j, our goal is to find a path that has a minimum cost.

import numpy as np
import copy

def shortpath(Path):
    nodes = len(Path[0,:])
    Pathback = np.random.random((nodes,nodes))
    while any(Path[i/nodes,i%nodes] != Pathback[i/nodes,i%nodes] for i in range(nodes*nodes)):
        Pathback = copy.deepcopy(Path)
        for k in range(nodes):
            for n in range(nodes):
                for m in range(nodes):
                    Path[n,m] = min(Path[n,m],(Path[n,k]+Path[k,m]))
    return Path

def pathview(Path, start, end):
    Pathchoice = [start, end]
    Pathchoiceback = [0]
    while len(Pathchoice) != len(Pathchoiceback):
        Pathchoiceback = copy.deepcopy(Pathchoice)
        for i in range(len(Pathchoice)-1):
            for k in range(Pathchoice[i]+1,Pathchoice[i+1]):
                if Path[Pathchoice[i],Pathchoice[i+1]] > (Path[Pathchoice[i],k]+Path[k,Pathchoice[i+1]]):
                    Pathchoice.insert(i+1,k)
                    print Pathchoice
    return Pathchoice

# test
nodes = 9
Pathtest = np.random.random((nodes,nodes))
for i in range(nodes):
    Pathtest[i,i] = 0
Pathtest[0, nodes-1] = 9
# print shortpath(Pathtest)
print pathview(Pathtest, 0, nodes-1)
Pathtest = np.array([[0,2,3,5],[3,0,1,2],[1,1,0,6],[2,3,1,0]])
# print shortpath(Pathtest)
print pathview(Pathtest, 0, 3)