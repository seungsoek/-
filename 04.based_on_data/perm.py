import itertools
import random

x= {'liverpool': [1,2,3], 'mancity': [1,2,3], 'tottenham': [1,2,3], 'westhame': [1,2,3]}

perm = itertools.permutations(x, 2)
perm = list(perm)
print(perm, len(perm))
