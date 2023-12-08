#%%

import utils
import re
import numpy as np
import matplotlib.pyplot as plt


lines = utils.readlines("6")

lines = [l.split(":")[1].strip() for l in lines]
# lines = [re.split("\ +", l) for l in lines]
# lines = [[int(i) for i in j] for j in lines]

lines = [[int(i.replace(" ", ""))] for i in lines]

times, dists = lines

print(lines)
beatable_options = []

for tmax, dist_min in zip(times, dists):
    n_beatable = 0
    # for t_push in range(1, tmax):
    #     def func(x): return t_push * x - t_push ** 2
        
    #     ls = np.linspace(0, tmax)
    #     #plt.plot(ls, func(ls), label=t_push)
    #     # print(tmax, dist_min, t_push)
    #     if func(tmax) > dist_min:
    #         n_beatable+=1
    

    # plt.hlines([dist_min], 0, tmax, "r")
    # plt.vlines([tmax], 0, dist_min, "r")
    # # plt.legend()
    # plt.show()
    # beatable_options.append(n_beatable)
    foo = []
    for i in [-1, 1]:
        p = -tmax
        q = dist_min
        foo.append(-(p/2) + i * np.sqrt((p/2)**2 - q))

    beatable_options.append(int(np.diff(foo)[0]))

print(np.prod(beatable_options))
# %%
