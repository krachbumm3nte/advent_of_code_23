# %%

import utils
import re
import numpy as np
import matplotlib.pyplot as plt

left = "SJ7-"
right = "SFL-"
up = "SLJ|"
down = "SF7|"


def valid_steps(map_, pos):
    x, y = pos
    l_pos = x, y - 1
    r_pos = x, y + 1
    u_pos = x-1, y
    d_pos = x+1, y

    return [p_new for p_new in (l_pos, r_pos, u_pos, d_pos) if is_path(pos, p_new, map_)]


def is_path(p1, p2, map_):

    x1, y1 = p1
    x2, y2 = p2

    char1 = map_[x1, y1]
    char2 = map_[x2, y2]

    if (x1 < x2 and char1 in down and char2 in up) or \
            (x1 > x2 and char1 in up and char2 in down) or \
            (y1 < y2 and char1 in right and char2 in left) or \
            (y1 > y2 and char1 in left and char2 in right):
        return True
    return False


lines = utils.readlines("10_ex3")
print(lines)

map_ = np.array([list(l) for l in lines])

map_ = np.pad(map_, 1, "constant", constant_values=["."])


start_idx = np.where(map_ == "S")
start_idx = start_idx[0][0], start_idx[1][0]


curr = valid_steps(map_, start_idx)[0]

n_steps = 0

trace = [start_idx]

while curr != start_idx:

    valid = valid_steps(map_, curr)
    # print(curr, valid, trace)
    next = valid[0] if valid[0] != trace[-1] else valid[1]

    trace.append(curr)
    curr = next
    n_steps += 1


tracemap = np.zeros_like(map_, dtype=bool)

for t in trace:
    tracemap[t[0], t[1]] = True

plt.imshow(tracemap)
plt.show()


n_inside = 0


inside_map = np.zeros_like(map_, dtype=bool)


trace_rows = np.where(np.any(tracemap, axis=1))[0]
x_start = trace_rows[1]
x_end = trace_rows[-2]

for x, row in enumerate(tracemap):

    if x < x_start: 
        continue
    if x >= x_end:
        break

    inside = True
    y_start = np.where(tracemap[x])
    y_start = y_start[0][0]
    for y, is_trace in enumerate(row):
        if y <= y_start:
            continue
        print(x, y, row[y-1], is_trace,  map_[x,y-1], map_[x,y], is_path((x,y), (x,y-1), map_))
        if (is_trace and not row[y-1]) or (is_trace and row[y-1] and not is_path((x,y), (x,y-1), map_)):
            inside = not inside
            print("toogle ", inside)
        
        if not is_trace and inside:
            print("is inside: ", (x,y))
            inside_map[x, y] = True
            n_inside += 1


print(n_inside)

plt.imshow(inside_map)
plt.show()
# %%
plt.plot([t[1] for t in trace], [map_.shape[0]-t[0] for t in trace])
plt.xlim(0, map_.shape[1])
plt.ylim(0, map_.shape[0])
plt.show()
# %%
print(map_)
# %%
print(len(trace))
# %%
print(len(trace)/2)
# %%
