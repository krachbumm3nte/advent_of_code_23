#%%
import utils
import re
import numpy as np
import matplotlib.pyplot as plt


lines = utils.readlines("3")

ar = np.array([list(l) for l in lines])


number_locs = np.vectorize(lambda x: bool(re.match(r"\d", x)))(ar)
blank_space = np.vectorize(lambda x: x == ".")(ar)
special_chars = np.logical_not(np.logical_or(number_locs, blank_space))

spec_x, spec_y = np.where(special_chars == True)


special_chars_mask = np.zeros_like(special_chars, dtype=bool)
for x,y in zip(spec_x, spec_y):
    special_chars_mask[x-1:x+2,y-1:y+2] = True


#plt.imshow(ar)
plt.imshow(number_locs)
plt.show()
plt.imshow(blank_space)
plt.show()
plt.imshow(special_chars)
plt.show()
plt.imshow(special_chars_mask)
plt.show()

part_digits = np.logical_and(special_chars_mask, number_locs)
plt.imshow(part_digits)
plt.show()

# %%

part_num_locs = []

dig_x, dig_y = np.where(part_digits == True)
for x, y in zip(dig_x, dig_y):
    ymin = y
    ymax = y
    i = y
    while number_locs[x,i]:
        ymin = i
        if i <= 0:
            break
        i-= 1

    i = y
    while number_locs[x,i]:
        i+= 1
        ymax = i
        if i == number_locs.shape[0]:
            break
    part_num_locs.append((x, ymin, ymax))
# %%
part_num_locs = set(part_num_locs)


part_nums = []

for (x, ymin, ymax) in part_num_locs:
    part_num = int("".join(ar[x, ymin:ymax]))
    part_nums.append(part_num)

sum(part_nums)

# %%


def is_adjacent(char, part_num):
    c_x, c_y = char
    p_x, p_ymin, p_ymax = part_num
    return abs(c_x-p_x) <= 1 and (c_y - p_ymax <= 0 and p_ymin - c_y <= 1)

stars_x, stars_y = np.where(ar == "*")
 
gear_ratios = []
for x,y in zip(stars_x, stars_y):
    adjacent_nums = []
    for num in part_num_locs:
        if is_adjacent((x,y), num):
            adjacent_nums.append(int("".join(ar[num[0], num[1]:num[2]])))
    if len(adjacent_nums) == 2:
        gear_ratios.append(adjacent_nums[0] * adjacent_nums[1])
# %%
print(sum(gear_ratios))
# %%
