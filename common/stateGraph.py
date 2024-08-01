from common.algebras import *
import itertools
import networkx as nx
import numpy as np


I = np.array([[1,0],[0,1]])
X = np.array([[0,1],[1,0]])
Y = np.array([[0,-1j],[1j,0]])
Z = np.array([[1,0],[0,-1]])

P_1 = {"I": I, "X": X, "Y": Y, "Z": Z}

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




P = P_1.keys() #strings
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

def stateGraph(algebraName, n):
    G_a = getAlgebra(algebraName)
    nodes = [''.join(x) for x in itertools.product('IXYZ', repeat=n)]

    E2 = E2_for_algebra(G_a)
    E = E2
    # print(E)
    for _ in range(n-2):
        E = [(P1+ p , P2+p) for p in P for (P1,P2) in E] + [ (p+P1 , p+P2)  for p in P for (P1,P2) in E]
    # print(E)
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(E)
    #print(sorted(nx.connected_components(G), key=len, reverse=True))
    #sorted_list = [len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
    #print(sorted_list)
    return sorted(nx.connected_components(G), key=len, reverse=True)

