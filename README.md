# Daily coding problem

this is a record of user mushcatshiro solving daily coding problem from dailycodingproblem.com. Content includes the user's answer, explanation and online best solution(not necessarily).
updates will not be frequent, expected to be in bulk.


## a guide to python function time complexity

| operation | Average Case | Amortized Worst Case |
|-----------|--------------|----------------------|
| copy | O(n) | O(n) |
| append | O(1) | O(1) |
| pop (last) | O(1) | O(1) |
| pop (intermediate) | O(k) | O(k)
| x in s | O(n) | - |
| min(s), max(s) | O(n) | - |
| len(s) | O(1) | O(1) |


## on utilities
utilities is a simple package create to reduce code required to be typed out. python module import will often encountered with ModuleNotFoundError if not handled properly. to mitigate this error create a file under LeetCode directory named config.py as follows,

```python
SYSPATH_DIR = "\\abs\\path\\to\\utilities"
```

and for every question that needs to import from utilities add the following code before importing

```python
import sys
from config import SYSPATH_DIR
sys.path.append(SYSPATH_DIR)
from utilities.data_structures import *
```