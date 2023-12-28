# %%

import utils
import re
import numpy as np


lines = utils.readlines("9")


next_vals = []
prev_vals = []
for l in lines:
    seq = [np.array([int(val) for val in l.strip().split(" ")])]

    while np.any(seq[-1] != 0):

        delta_s = []
        s = seq[-1]

        for i in range(len(s) - 1):
            delta_s.append(s[i+1] - s[i])

        seq.append(np.array(delta_s))

    v_next = 0
    v_prev = 0
    for s2 in seq[-2::-1]:
        v_next += s2[-1]
        v_prev = s2[0] - v_prev

    next_vals.append(v_next)
    prev_vals.append(v_prev)

print(sum(next_vals))
print(sum(prev_vals))
# %%
