import numpy as np
from scipy.linalg import expm
import random
from functools import reduce
from numpy.random import uniform
import itertools
import networkx as nx
from tabulate import tabulate

I = np.array([[1,0],[0,1]])
X = np.array([[0,1],[1,0]])
Y = np.array([[0,-1j],[1j,0]])
Z = np.array([[1,0],[0,-1]])

P_1 = {"I": I, "X": X, "Y": Y, "Z": Z}
P_2 = np.array([np.kron(a,b) for a in P_1.values() for b in P_1.values() ]) # probably there is a more efficient way to generate u(4) not using all basis elements
#II,IX,IY,IZ, XI,XX,XY,XZ, YI, YX,YY,YZ, ZI, ZX, ZY, ZZ  matrices

G = [ ["XX"], #0
     ["XY"], #1
     ["XY", "YX"], #2
     ["XX", "YZ"], #3
     ["XX", "YY"], #4
     ["XY", "YZ"], #5
     ["XX","YZ","ZY"],#6
     ["XX", "YY","ZZ"],#7
     ["XX", "XZ"],#8
     ["XY", "XZ"],#9
     ["XY", "YZ", "ZX"],#10
     ["XY", "YX", "YZ"],#11
     ["XX", "XY", "YZ"],#12
     ["XX", "YY", "YZ"],#13
     ["XX", "YY", "XY"],#14
     ["XX", "XY", "XZ"],#15
     ["XY", "YX", "YZ", "ZY"],#16
     ["XX", "XY", "ZX" ], #17
     ["XX", "XZ", "YY", "ZY"], #18
     ["XX", "XY", "ZX", "YZ"], #19
     ["XX", "YY", "ZZ", "ZY"],#20
     ["XX", "YY", "XY", "ZX"], #21
     [ "XX", "XY", "XZ", "YX"], #22
     [ "XI", "IX"], #b0
     [ "XX", "XI", "IX"], #b1
     [ "XY", "XI", "IX"],#b2
     [ "XI", "YI", "IX", "IY"], #b3
     [ "XX", "XY", "XZ", "XI", "IX", "IY", "IZ"] #b4
     ]

idx_exp = [5,6,7,9,10,11,12,13,15,16,17,18,19,20,21,22,25,27]

generator_set_matrices =[[np.kron(P_1[s[0]], P_1[s[1]]) for s in G_a] for G_a in G]
generator_set_matrices += [P_2] # adding generators for entire unitary group
zero = [1,0]
one = [0,1]
zero_state = np.kron(zero,zero)
X_space = [np.kron(a,b) for a in [zero, one] for b in [zero, one]]
Z_expectation_list = []

idx_parity = [0,1,2,4,7,14] # algebras with ZZ in the commutator and hence avergae beeing the uniform probability distribution supported on the even bitstrings
tvd_means = []
for idx, A in enumerate(generator_set_matrices):
    Z_list = []
    tvd_list = []
    for _ in range(1000): # average over 1000 unitaries
        params = np.array([uniform(-np.pi, np.pi) for _ in range(len(A))])
        U_k_list = [expm(1j * params[i] * A[i]) for i in range(len(A))]
        U_list = random.choices(U_k_list, k=100)
        U = reduce(np.dot, U_list) #one element of the group
        Z=0 # compute the collision probability for that unitary
        p = []
        for x in X_space:
            B = U.dot(zero_state)
            Z += np.abs(np.inner(x, B)) ** 4  # sum over x
            p.append(np.abs(np.inner(x, B)) ** 2)
        if not idx in idx_parity:
            tvd_list.append(0.5 * np.sum(np.abs(np.array(p) - 1 / 4)))
        else:
            if np.any(np.all(x == [np.kron(zero,zero), np.kron(one,one)], axis=1)):
                tvd_list.append(0.5 * np.sum(np.abs(np.array(p) - 1 / 2)))
            else:
                tvd_list.append(0.5 * np.sum(np.abs(np.array(p))))

        Z_list.append(Z)
    tvd_means.append(np.mean(tvd_list))
    Z_expectation_list.append(np.round(np.mean(Z_list),3))
print(Z_expectation_list)
print(np.round(tvd_means,3))


Z = [0.767, 0.752, 0.752, 0.556, 0.75, 0.547, 0.443, 0.752, 0.52, 0.522, 0.439, 0.517, 0.505, 0.526, 0.674, 0.444, 0.497, 0.445, 0.514, 0.431, 0.449, 0.446, 0.426, 0.558, 0.439, 0.503, 0.463, 0.419, 0.404]
TVD = [0.831, 0.82 , 0.82,  0.458 ,0.817, 0.449 ,0.347, 0.82,  0.428, 0.431, 0.341, 0.427,0.417 ,0.435 ,0.754 ,0.36  ,0.411 ,0.36 , 0.425 ,0.348, 0.362, 0.359, 0.34 , 0.461
, 0.339, 0.417 ,0.379, 0.336 ,0.322]
data = dict()
data["Algebra"] =["$A_0$", "$A_1$" ,"$A_2$" ,"$A_3$", "$A_4$", "$A_5$", "$A_6$", "$A_7$", "$A_8$", "$A_9$","$A_{10}$",  "$A_{11}$" ,  "$A_{12}$" , "$A_{13}$" , "$A_{14}$"  , "$A_{15}$",
         "$A_{16}$", "$A_{17}$" , "$A_{18}$",  "$A_{19}$",  "$A_{20}$", "$A_{21}$", "$A_{22}$",  "$B_0$",  "$B_1$",  "$B_2$", "$B_3$", "$B_4$", "$P_2$"]
data["Z"] = Z
data["TVD"] = TVD
df = pd.DataFrame(data)
latex_table = df.to_latex(index=False, float_format="{:0.2f}".format)
print(latex_table)

P = P_1.keys() #strings
n = 10 #dimension for the commutator graph
nodes = [''.join(x) for x in itertools.product('IXYZ', repeat=n)]
# every generator induces 4 edges for n = 2 # n²?
E2_per_Pauli = {
"IX" : [("ZY", "ZZ"), ("XY", "XZ"), ("YZ", "YY"), ("IZ", "IY")],
"IY" : [("IX", "IZ"), ("XX", "XZ"), ("YX", "YZ"), ("ZX", "ZZ")],
"IZ" : [("IX", "IY"), ("XX", "XY"), ("ZX", "ZY"), ("YX", "YY")],
"XI" : [("ZY", "YY"), ("ZX", "YX"), ("ZZ", "YZ"), ("ZI", "YI")],
"XX" : [("XZ", "IY"), ("IZ", "XY"), ("ZI", "YX"), ("YI", "ZX")],
"XY" : [("IX", "XZ"), ("IZ", "XX"), ("YI", "ZY"), ("YY", "ZI")],
"XZ" : [("IX", "XY"), ("IY", "XX"), ("YI", "ZZ"), ("YZ", "ZI")],
"YI" : [("XX", "ZX"), ("XY", "ZY"), ("XZ", "ZZ"), ("ZI", "XI")],
"YX": [("IY","YZ"),("IZ","YY"),("ZI","XX"),("ZX","XI")],
"YY" : [("YX","IZ"),("ZI","XY"),("ZY","XI"),("IX","YZ")],
"YZ" : [("IY","YX"),("ZZ","XI"),("ZI","XZ"),("YY","IX")],
"ZX" : [("ZY","IZ"),("YI","XX"),("IY","ZZ"),("YX","XI")],
"ZY" : [("ZX","IZ"),("YI","XY"),("XI","YY"),("IX","ZZ")],
"ZZ": [("XZ","YI"),("IY","ZX"),("ZY","IX"),("XI","YZ")]}


def E2_for_algebra(G):
    E_sub = []
    for s in G:
        E_sub += E2_per_Pauli[s]
    return E_sub

for G_a in G:
    E2 = E2_for_algebra(G_a)
    E = E2
    for _ in range(n-2):
        E = [(P1+ p , P2+p) for p in P for (P1,P2) in E] + [ (p+P1 , p+P2)  for p in P for (P1,P2) in E]
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(E)
    sorted_list = [len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
    print(sorted_list)

