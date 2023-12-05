#%%
import utils
import re
import numpy as np

lines = utils.readlines("4")

pts = []
for l in lines:
    l = l.split(":")[1]

    my_nums, winning_nums = l.split("|")
    my_nums = [int(i) for i in re.split(r"\ +", my_nums.strip())]
    winning_nums = [int(i) for i in re.split(r"\ +", winning_nums.strip())]

    n_common = len(set(my_nums) & set(winning_nums))
    if n_common > 0:
        pts.append(2**(n_common-1))
print(sum(pts))
# %%



pts = np.ones(len(lines))


for i, l in enumerate(lines):
    l = l.split(":")[1]

    my_nums, winning_nums = l.split("|")
    my_nums = [int(i) for i in re.split(r"\ +", my_nums.strip())]
    winning_nums = [int(i) for i in re.split(r"\ +", winning_nums.strip())]

    n_common = len(set(my_nums) & set(winning_nums))
    print(n_common)
    if n_common > 0:
        pts[i+1:i+1+n_common] += pts[i]
    
    print(pts)
print(sum(pts))
# %%
