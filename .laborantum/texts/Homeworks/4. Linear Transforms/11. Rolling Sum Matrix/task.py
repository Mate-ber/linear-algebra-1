#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

path = Path(".laborantum/texts/Homeworks/4. Linear Transforms/11. Rolling Sum Matrix")

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[2]:


import numpy as np

def rolling_sum(N):
    # YOUR CODE HERE
    A = np.zeros((N, N))
    
    # Fill the matrix such that A[i, j] = 1 for j <= i
    for i in range(N):
        for j in range(i + 1):
            A[i, j] = 1
    
    return A
    return 0


# In[3]:


import time

start = time.time()

debug_result = [rolling_sum(**x) for x in debug_cases]
answer = [rolling_sum(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[ ]:




