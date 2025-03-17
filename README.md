# PauLie
The `PauLie` package is an open-source library for studying various algebraic properties of quantum circuits.  This
first release focuses on the classification of the circuit's dynamical Lie algebra given the generators as Paulistrings.

<p align="center">
  <a href="https://qpaulie.github.io/PauLie/">
  <img width=30% src="https://img.shields.io/badge/documentation-blue?style=for-the-badge&logo=read%20the%20docs" alt="Documentation" />
  </a>
</p>


[![Unitary Fund](https://img.shields.io/badge/Supported%20By-UNITARY%20FUND-brightgreen.svg?style=for-the-badge)](https://unitary.fund)

Make sure to have Python >= 3.12 installed.

### Installation
Clone the repository. Once you have [`poetry` installed](https://python-poetry.org/docs/#installation), run:

```sh
poetry install
poetry shell
```

### Getting started 

The following code gives an example of usage:

```python
    from paulie.application.classify import get_algebra
    n_qubits = 6
    generators = ["XYZXZZ", "ZZYZY"]
    algebra = get_algebra(generators, size = n_qubits)
    print(f"number of qubits = {n_qubits}, algebra = {algebra}")
```

Feel free to contribute and check out our open issues. We are also happy to chat with you via [Dicord](https://discord.gg/unitary-fund-764231928676089909)

### Testing

In order to run the test suite, run:

```sh
poetry run python -m pytest
```


