# Maximum Flow
import numpy as np
import copy

# A depth-first path-finding function
def Findpath(Flow,s,t):
    path = [s]
    falsepath = [s]
    nodes = len(Flow[0])
    check = 0
    while path[-1]!=t and check < nodes*nodes:
        check += 1
        subcheck = 0
        for i in range(nodes):
            if Flow[path[-1],i]>0 and subcheck == 0 and i not in path and i not in falsepath:
                path.insert(len(path),i)
                subcheck = 1
        if subcheck == 0 and len(path) > 1:
            falsepath.insert(len(falsepath),path[-1])
            del path[-1]
        # print path
        # print path[-1]!=t
    return path

# find the minimum flow along a certain path
def Findminflow(Flow, path):
    if len(path) > 1:
        minflow = Flow[path[0],path[1]]
        for i in range(len(path)-2):
            if Flow[path[i+1],path[i+2]]<minflow:
                minflow = Flow[path[i+1],path[i+2]]
    else:
        minflow = 0
    return minflow

# Find the maximum flow for the graph denoted by Flowtest:
A = 0
Flowtest = np.array([[A,8,7,A,A,A],[A,A,A,6,A,A],[A,2,A,A,6,A],[A,A,9,A,A,10],[A,A,A,5,A,2],[A,A,A,A,A,A]])  # the test graph 1
CurrentFlow = np.array([[A,A,A,A,A,A],[A,A,A,A,A,A],[A,A,A,A,A,A],[A,A,A,A,A,A],[A,A,A,A,A,A],[A,A,A,A,A,A]])
resFlow = copy.deepcopy(Flowtest)
# Flowtest = np.array([[A,1000,1000,A],[A,A,1,1000],[A,A,A,1000],[A,A,A,A]])  # the test graph 2
# resFlow = copy.deepcopy(Flowtest)
# CurrentFlow = np.array([[A,A,A,A],[A,A,A,A],[A,A,A,A],[A,A,A,A]])
s = 0
t = len(Flowtest[0])-1
CurrentPath = Findpath(resFlow,s,t)
f = Findminflow(resFlow, Findpath(resFlow,s,t))
while(CurrentPath[-1]==t):
    for k in range(len(CurrentPath)-1):
        CurrentFlow[CurrentPath[k], CurrentPath[k+1]] += f
        if CurrentFlow[CurrentPath[k+1], CurrentPath[k]]-f > 0:
            CurrentFlow[CurrentPath[k+1], CurrentPath[k]] -= f
        else:
            CurrentFlow[CurrentPath[k+1], CurrentPath[k]] -= 0
    for i in range(len(CurrentFlow)):
        for j in range(len(CurrentFlow[i])):
            if CurrentFlow[i,j] > 0:
                resFlow[i,j] = Flowtest[i,j]-CurrentFlow[i,j]
                resFlow[j,i] = CurrentFlow[i, j]
    CurrentPath = Findpath(resFlow,s,t)
    f = Findminflow(resFlow, Findpath(resFlow,s,t))
print CurrentFlow  # the final maximum flow for the test graph
