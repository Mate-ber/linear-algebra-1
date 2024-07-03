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

path = Path(".laborantum/texts/Homeworks/4. Linear Transforms/8. Gramm Matrix II")

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[2]:


import numpy as np

def co_to_contra(B, x):
    # YOUR CODE HERE
    B_T = B.T
    B_inv = np.linalg.inv(B)
    cov = np.dot(B_inv, x)
    res = np.dot(B_T, cov)
    
    return res


# In[3]:


import time

start = time.time()

debug_result = [co_to_contra(**x) for x in debug_cases]
answer = [co_to_contra(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[ ]:




