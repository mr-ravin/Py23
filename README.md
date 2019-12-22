# Py23
This repository provides a simplebut effective OpenSource Parser to convert Python2 source code into Python3 source code. It is a very simple library, more functions will get added depending on the opensource collaborations, and user experiences.

#### Code Develper: [Ravin Kumar](https://mr-ravin.github.io)

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

```python
Copyright (c) 2019 Ravin Kumar
Website: https://mr-ravin.github.io

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation 
files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, 
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the 
Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
