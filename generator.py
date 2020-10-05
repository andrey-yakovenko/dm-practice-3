import random
import itertools
import pandas as pd
import numpy as np

VOTERS_NUMBER = 75
CANDIDATES_NUMBER = 5

# Code below generates random set of preferences to the "data.csv" file accordingly to parameters above
preferences = []
t = list(itertools.permutations('12345', CANDIDATES_NUMBER))
for i in range(VOTERS_NUMBER):
    index = random.randint(1, len(t)-1)
    p = ''.join(str(e) for e in t[index])
    preferences.append(p)
data = pd.DataFrame(np.array(preferences), columns=["preferences"])
data.to_csv('data.csv')
