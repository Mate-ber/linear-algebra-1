#!/usr/bin/env python
# coding: utf-8

# In[16]:


get_ipython().run_line_magic('reload_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')

import sys
sys.path.append('../../../../../code/')
sys.path.append('code')


# In[17]:


from invert_matrix import invert_matrix
import numpy as np



# In[18]:


import sys
import os
from pathlib import Path
import json_tricks

path = Path('.').resolve()

index = str(path).find('.laborantum')

if index > 0:
    path = str(path)[:index]

os.chdir(path)

path = Path('.laborantum/texts/Homeworks/5. Gauss Algorithm/4. Matrix Inversion')

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# print(public_cases)


# In[19]:


import time

start = time.time()

debug_result = [invert_matrix(**x) for x in debug_cases]
answer = [invert_matrix(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[20]:


print("Checking misfits |Ax - b|:")
print("Misfit should be < 1.0e-8")
print()
print('=' * 5 + ' DEBUG CASES ' + '='*5)
for index in range(len(debug_result)):
    case = debug_cases[index]
    A_inv = debug_result[index]

    A = case['A']
    # b = case['b']
    print(
        'Case #' + str(index),
        np.abs(A.astype(float) @ A_inv - np.eye(A.shape[0])).sum())
    

print()
print('=' * 5 + ' TEST CASES ' + '=' * 5)
for index in range(len(answer)):
    case = public_cases[index]
    A_inv = answer[index]

    A = case['A']
    # b = case['b']

    # print(A)
    # print(numpy.linalg.inv(A))
    # print(numpy.linalg.det(A))

    # print(A.shape, A_inv.shape)
    print(
        'Case #' + str(index),
        np.abs(A.astype(float) @ A_inv - np.eye(A.shape[0])).sum())
print('=' * 5 + ' END ' + '=' * 5)


# In[ ]:




