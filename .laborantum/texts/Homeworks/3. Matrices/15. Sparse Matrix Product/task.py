#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().run_line_magic('reload_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')

import sys
import os
from pathlib import Path
import json_tricks

path = Path('.').resolve()

index = str(path).find('.laborantum')

if index > 0:
    path = str(path)[:index]

os.chdir(path)

path = Path(".laborantum/texts/Homeworks/3. Matrices/15. Sparse Matrix Product")

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[5]:


import numpy as np
from collections import defaultdict

def sparseProduct(A, B):
    # YOUR CODE HERE
    res = np.zeros(A.shape)
    
    c_map = defaultdict(dict)
    
    for r, c, v in B:
        c_map[c][r] = v
    
    for col in c_map:
        for row_A in range(A.shape[0]):
            if col in range(A.shape[0]):
                for row_B in c_map[col]:
                    res[row_A, col] += A[row_A, row_B] * c_map[col][row_B]
    
    return res


# In[6]:


import time

start = time.time()

debug_result = [sparseProduct(**x) for x in debug_cases]
answer = [sparseProduct(**x) for x in public_cases]

print(answer)

print(time.time() - start, '<- Elapsed time')

