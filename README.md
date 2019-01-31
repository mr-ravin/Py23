# Py23
This repository provides a simplebut effective OpenSource Parser to convert Python2 source code into Python3 source code. It is a very simple library, more functions will get added depending on the opensource collaborations, and user experiences.

### Working Demonstration

To better understand the functioning of this very simple but effective library, we have provided a demo example:
Consider you want to source code of python2 File: python2code.py into its Python 3 equivalent.

- Case 1: When we want to override the existing file.
```python
import py23
py23.convert("python2code.py")
```
- Case 2: When we want to create a new file for converted code.
```python
import py23
py23.convert("python2code.py","python3code.py") ## it will save the python3 equivalent code into python3code.py file.
```
