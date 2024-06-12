#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
import json_tricks
import os

numpy.random.seed(42)

debug_cases = []
for index in range(20):
    N = numpy.random.randint(1, 20, size=[1])[0]
    debug_cases.append({'N': N})

os.makedirs('testcases', exist_ok=True)
with open('testcases/debug_cases.json', 'w+') as fin:
    fin.write(json_tricks.dumps(debug_cases))

public_cases = []
for index in range(20):
    N = numpy.random.randint(1, 20, size=[1])[0]
    public_cases.append({'N': N})

with open('testcases/public_cases.json', 'w+') as fin:
    fin.write(json_tricks.dumps(public_cases))


# In[2]:


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

path = Path(".laborantum/texts/Homeworks/4. Linear Transforms/12. Neighbors Difference Matrix")

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[15]:


import numpy as np

def diff(N):
    res = np.zeros([N-1, N])
    for index in range(N-1):
        for index2 in range(N):
            if index2 == index:
                res[index, index2] = -1
            if index2 == index + 1:
                res[index, index2] = 1
    return res


# In[16]:


import time

start = time.time()

debug_result = [diff(**x) for x in debug_cases]
answer = [diff(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[ ]:




