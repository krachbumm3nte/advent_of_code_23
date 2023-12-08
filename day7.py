# %%

import utils
import re
import numpy as np
import matplotlib.pyplot as plt
import functools
from collections import Counter

lines = utils.readlines("7")
lines = [l.split(" ") for l in lines]

ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


# %%


def comp(x, y):
    hand1 = x[0]
    hand2 = y[0]
    n_max1 = Counter(hand1).most_common(1)[0][1]
    n_max2 = Counter(hand2).most_common(1)[0][1]

    if n_max1 != n_max2:
        return n_max2 - n_max1
    rank1 = len(set(hand1))
    rank2 = len(set(hand2))
    if rank1 != rank2:
        # print("rank", rank1, rank2)
        return rank1 - rank2
    else:
        for i in range(len(hand1)):
            val1 = ranks.index(hand1[i])
            val2 = ranks.index(hand2[i])

            if val1 != val2:
                return val1 - val2
    return 0


ascending = sorted(lines, key=functools.cmp_to_key(comp), reverse=True)

sum_winnings = 0

for i in range(len(ascending)):
    val = int(ascending[i][1])
    sum_winnings += (i + 1) * val

print(sum_winnings)
# %%


def comp(x, y):
    hand1 = x[0]
    hand2 = y[0]

    counts1 = Counter(hand1)
    counts2 = Counter(hand2)

    jokers_1 = counts1.get("J", 0)
    jokers_2 = counts2.get("J", 0)

    n_max1 = counts1.most_common(1)[0][1] + jokers_1
    n_max2 = counts2.most_common(1)[0][1] + jokers_2

    if n_max1 != n_max2:
        return n_max2 - n_max1
    rank1 = len(set(hand1)) - jokers_1
    rank2 = len(set(hand2)) - jokers_2
    if rank1 != rank2:
        # print("rank", rank1, rank2)
        return rank1 - rank2
    else:
        for i in range(len(hand1)):
            val1 = ranks.index(hand1[i])
            val2 = ranks.index(hand2[i])

            if val1 != val2:
                return val1 - val2
    return 0


ascending = sorted(lines, key=functools.cmp_to_key(comp), reverse=True)

sum_winnings = 0

for i in range(len(ascending)):
    val = int(ascending[i][1])
    sum_winnings += (i + 1) * val

print(sum_winnings)
# %%
