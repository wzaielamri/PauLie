.. _getting_started_reference-label:

===============
Getting started
===============
----------
Installing
----------
1. Install the package builder
.. code-block:: bash
    python3 -m pip install --upgrade build
2. Build
.. code-block:: bash
    python3 -m build

3. Install the assembled package
.. code-block:: bash
    python -m pip install -e .

4. Install external dependencies
.. code-block:: bash
    pip install -r requirements.txt