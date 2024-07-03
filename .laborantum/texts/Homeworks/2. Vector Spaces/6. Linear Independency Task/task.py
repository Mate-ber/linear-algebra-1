#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('reload_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')

import sys
import os
from pathlib import Path

path = Path('.').resolve()

index = str(path).find('.laborantum')

if index > 0:
    path = str(path)[:index]

os.chdir(path)

get_ipython().system('{sys.executable} -m pip -q install --user numpy json-tricks torch jupyter nbconvert')


# In[2]:


import json_tricks

path = Path('.laborantum/texts/Homeworks/2. Vector Spaces/6. Linear Independency Task')

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[3]:


import numpy as np


def is_independent(A):
    ## YOUR CODE HERE
    
    Q, R = np.linalg.qr(A)

    if len(Q) != len(Q[0]):
        return False

    for i in range(len(Q)):
        if abs(R[i][i]) <= 1e-5:
            return False


    return True


# In[4]:


import time

start = time.time()

debug_result = [is_independent(**x) for x in debug_cases]
answer = [is_independent(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')

