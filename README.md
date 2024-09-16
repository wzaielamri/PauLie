# Lie_props
Moment calculation over quantum circuits given their generators. 

[![Unitary Fund](https://img.shields.io/badge/Supported%20By-UNITARY%20FUND-brightgreen.svg?style=for-the-badge)](https://unitary.fund)

### Installation
pip install -r requirements.txt

### Description

#### 1. momentumAlgebras.py
Calculations, for all algebra generators it calculates EZ with sizes from 2 to 5

#### 2. classifyAlgebras.oy
Classification of all algebras of size 8.

#### 3. plotCanonic.oy
Reducing the algebra a6 generator graph of size 8 and plotting the result

#### 4. animationCanonic.oy
Reducing the algebra a6 generator graph of size 8 and animating its construction

#### 7. common/pauli.py
Implementation of a Pauli string based on bitarray. Basic operations on Pauli strings: creation, incrementation, multiplication, commutation, comparison, conversion to string

#### 8. common/generator.py
Pauli string generators, based on algebra generators.

#### 9. common/algebras.py
Algebra generators

#### 10. common/commutatorGraph.py
Construction of a commutative graph that is complete and intersects with {I,Z}^n

#### 11. common/stateGraph.py
Construction of a complete graph based on the networkx library. Needed to compare the results of constructing a graph on commutators.

#### 12. common/storage/EdgeStorage.py
An abstract class for storing the results of constructing a graph.

#### 13. common/storage/impl/EdgeStorageArray.py
Implementation of an abstract class for storing the results of constructing a graph in an array. Needed for fine debugging of subgraph vertex values

#### classifier
The folder contains files for reducing a set of generators to a canonical graph

#### 14. classifier/subgraphs.py
Partitioning the generator graph into connected subgraphs

#### 15. classifier/transform.py
Basic algorithm for converting the original graph to a cononical type

#### 16. classifier/shape.py
Contains a class responsible for controlling the construction of a graph in cononical form. Is the result of the cononic type casting algorithm

#### 17. classifier/printing.py
Functions and class responsible for outputting data when running the algorithm in debugging mode.

#### 18. classifier/graphView.py
Converting a set of nodes into data for constructing a graph (nodes, edges, labels for edges).

#### 19. classifier/recording.py
Classes and functions for recording the graph construction process

#### 20. classifier/drawing.py
Graph drawing and animation functions






