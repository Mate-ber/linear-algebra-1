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

path = Path(".laborantum/texts/Homeworks/3. Matrices/14. Diagonal Matrices Product")

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[2]:


import numpy as np

def DA_AD_product(D, A):
    # YOUR CODE HERE
    if len(D.shape) == 1:
        D = np.diag(D)
    
    # DA: Multiply each row of A by the corresponding diagonal element of D
    DA = D @ A
    
    # AD: Multiply each column of A by the corresponding diagonal element of D
    AD = A @ D
    
    res = {
        'DA': DA,
        'AD': AD
    }
    return res


# In[3]:


import time

start = time.time()

debug_result = [DA_AD_product(**x) for x in debug_cases]
answer = [DA_AD_product(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[ ]:



