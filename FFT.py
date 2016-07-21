# convolution can be used in computing the multiplcation of two polynomials,
# e.g, A=[1, 4, 2, 0, 2], B=[3, 1, 2]
# The convolution of A and B is another polynomial C, with its coefficients C_k= \Sigma A_i*B_{k-i}(for i in range(k))

import numpy as np
import math
import copy

def convolution(A, B):
    C = [0]*(len(A)+len(B)-1)
    for i in range(len(C)):
        for j in range(max(i-len(B)+1, 0) ,min(i+1, len(A))):
            C[i] += A[j] * B[i-j]
    return C

A=[1, 4, 2, 0, 2]
B=[3, 1, 2]
print "Convolution:", convolution(A, B)

# FFT transfers the coefficients of a polynomial A to a set of values for certain variables. 
# Given all the coefficients, a polynomial is fixed, meanwhile given enough 
# variables(equal to the number of coefficients), a polynomial is all fixed.
# Deriving results for a full set of variables from all the coefficients can be easily done through
# choosing some special variables. In the FFT method, we choose the variables to be N root of unity,
#  where N is a power of 2 and it corresponds to the highest orders of the polynomial (or highest order plus one if odd).

def OofU(n):  # generate a set of nth order root of unity
    w = [0] * n
    for i in range(n):
        w[i] = np.exp(2.0*np.pi*complex(0,(i+0.0)/n))
    return w

def OofUrev(n):  # generate a set of nth order root of unity
    w = [0] * n
    for i in range(n):
        w[i] = np.exp(-2.0*np.pi*complex(0,(i+0.0)/n))
    return w
# print OofU(2)

def butterflyid(n):  # generate a binary index for butterfly network
    bid = {}
    for i in range(2**n):
        bid[str(2**n-i-1)] = '0'*(n-len(bin(2**n-1-i)[2:]))+bin(2**n-1-i)[2:]
    return bid

def butterflyidrev(n):  # generate a binary index for butterfly network
    bid = {}
    for i in range(2**n):
        bid[(2**n-i-1)] = int(('0'*(n-len(bin(2**n-1-i)[2:]))+bin(2**n-1-i)[2:])[::-1],2)
    bid = {value:key for key, value in bid.items()}
    return bid

# rev = butterflyidrev(5)
# print rev
# print type(rev[3])

def FFT(A):
    logN = int(math.ceil(np.log2(len(A))))
    N = 2**logN
    ind = butterflyidrev(logN)
    A.extend([0] * (N - len(A)))
    Aco = copy.deepcopy(A)
    subsec = 1
    interval = 2
    while N >= 1:
        N = N / 2
        w = OofU(interval)
        for i in range(N):
            for j in range(subsec):
                # print interval*i+j, j, j+subsec
                if subsec == 1:
                    Aco[interval*i+j] = A[ind[interval*i+j]] + w[j]*A[ind[interval*i+subsec+j]]
                    Aco[interval*i+subsec+j] = A[ind[interval*i+j]] + w[j+subsec]*A[ind[interval*i+subsec+j]]
                else:
                    Aco[interval*i+j] = A[interval*i+j] + w[j]*A[interval*i+subsec+j]
                    Aco[interval*i+subsec+j] = A[interval*i+j] + w[j+subsec]*A[interval*i+subsec+j]
        interval = interval * 2
        subsec = subsec * 2
        A = copy.deepcopy(Aco)
    return Aco

def revFFT(A):
    logN = int(math.ceil(np.log2(len(A))))
    N = 2**logN
    ind = butterflyidrev(logN)
    A.extend([0] * (N - len(A)))
    Aco = copy.deepcopy(A)
    subsec = 1
    interval = 2
    while N >= 1:
        N = N / 2
        w = OofUrev(interval)
        for i in range(N):
            for j in range(subsec):
                # print interval*i+j, j, j+subsec
                if subsec == 1:
                    Aco[interval*i+j] = (A[ind[interval*i+j]] + w[j]*A[ind[interval*i+subsec+j]])
                    Aco[interval*i+subsec+j] = (A[ind[interval*i+j]] + w[j+subsec]*A[ind[interval*i+subsec+j]])
                else:
                    Aco[interval*i+j] = (A[interval*i+j] + w[j]*A[interval*i+subsec+j])
                    Aco[interval*i+subsec+j] = (A[interval*i+j] + w[j+subsec]*A[interval*i+subsec+j])
        interval = interval * 2
        subsec = subsec * 2
        A = copy.deepcopy(Aco)
    for i in range(len(Aco)):
        Aco[i] = Aco[i]/4.0
    return Aco

print "FFT:", FFT([1,0,1,-1])
print "Inversed FFT:", revFFT([5,complex(4,-1),-1,complex(4,1)])