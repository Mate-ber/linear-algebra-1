#!/usr/bin/env python
# coding: utf-8

# In[27]:


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

path = Path('.laborantum/texts/Homeworks/3. Matrices/11. Numpy Matrix Expression')

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[28]:


import numpy as np

def formula(A, B, C, x):
    # YOUR CODE HERE
    A_T = A.T
    # B= A_T @ B
    # C= A_T @ (C)
    B_2C = B + 2 * C

    A_T_B_2C = A_T @ B_2C

    for i in range(min( len(A_T_B_2C),len(A_T_B_2C[0]))):
        A_T_B_2C[i][i] += 3

    M = A_T_B_2C

    exp_M = np.exp(M)

    result = exp_M @ x
    
    return result


# In[29]:


import time

start = time.time()

debug_result = [formula(**x) for x in debug_cases]
answer = [formula(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[ ]:




