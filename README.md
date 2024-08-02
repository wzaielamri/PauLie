# Lie_props
Moment calculation over quantum circuits given their generators. 

[![Unitary Fund](https://img.shields.io/badge/Supported%20By-UNITARY%20FUND-brightgreen.svg?style=for-the-badge)](https://unitary.fund)

### Installation
pip install -r requirements.txt

### Description

#### 1. test.py
Testing calculations, for all algebra generators it calculates EZ with sizes from 2 to 5
For algebra, a0 does calculations from 2 to 8, as well as calculations of size 10. This is runtime testing.

#### 2. common/pauli.py
Implementation of a Pauli string based on bitarray. Basic operations on Pauli strings: creation, incrementation, multiplication, commutation, comparison, conversion to string

#### 3. common/generator.py
Pauli string generators, based on algebra generators.

#### 4. common/algebras.py
Algebra generators

#### 5. common/commutatorGraph.py
Construction of a commutative graph that is complete and intersects with {I,Z}^n

#### 6. common/stateGraph.py
Construction of a complete graph based on the networkx library. Needed to compare the results of constructing a graph on commutators.

#### 7. common/storage/EdgeStorage.py
An abstract class for storing the results of constructing a graph.

#### 8. common/storage/impl/EdgeStorageArray.py
Implementation of an abstract class for storing the results of constructing a graph in an array. Needed for fine debugging of subgraph vertex values