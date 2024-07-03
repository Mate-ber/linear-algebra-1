#!/usr/bin/env python
# coding: utf-8

# In[51]:


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


# In[52]:


import json_tricks

path = Path('.laborantum/texts/Homeworks/1. Vectors/33. Exercise Vectors 3')


# In[53]:


debug_cases = json_tricks.load(str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(str(path / 'testcases' / 'public_cases.json'))


# In[54]:


import numpy as np
import numpy.typing as npt
from typing import Dict

def vector_operations(x, y):
    ## YOUR CODE HERE
    exp = (2 * x) + y
    dot_prod = np.dot(x, y)
        
    length_x = np.linalg.norm(x)
    length_y = np.linalg.norm(y)
    angle = np.arccos(dot_prod / (length_x * length_y))

    dir_a = np.copy(x)
    dir_b = np.copy(y)

    for i in range(len(dir_a)):
        dir_a[i] = dir_a[i] / length_x
        dir_b[i] = dir_b[i] / length_y


    a_proj_b = (dot_prod / length_y * length_y) * y
    b_proj_a = (dot_prod / length_x * length_x) * x
    
    a_orth_b = y - a_proj_b
    b_orth_a = x - b_proj_a

    answer = {
        'expression': np.array(exp),
        'dot_prod': dot_prod,
        'length_a': length_x,
        'length_b': length_y,
        'angle': angle,
        'dir_a': np.array(dir_a),
        'dir_b': np.array(dir_b),
        'a_proj_b': np.array(a_proj_b),
        'b_proj_a': np.array(b_proj_a),
        'a_orth_b': np.array(a_orth_b),
        'b_orth_a': np.array(b_orth_a)
    }
    
    return answer


# In[55]:


import time

start = time.time()

debug_result = [vector_operations(**x) for x in debug_cases]
answer = [vector_operations(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')

