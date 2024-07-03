#!/usr/bin/env python
# coding: utf-8

# In[78]:


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

path = Path(".laborantum/texts/Homeworks/3. Matrices/12. Einstein's Rule")

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[79]:


import numpy as np

def formula(A, B, C, D):
    # YOUR CODE HERE
    # res1 = np.einsum('mn, no->', B, C)
    
    # res2 = np.einsum('lk, km->', D, A)

    # res = res.T
    # #D = D.T

    res = np.einsum('km,mn,no,lk->', A, B,C,D)

    #print(res1*res2)
    #print(res)

    
    return res


# In[80]:


import time

start = time.time()

debug_result = [formula(**x) for x in debug_cases]
answer = [formula(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[ ]:




