#%%
import utils
import re
import numpy as np
import matplotlib.pyplot as plt


lines = utils.readlines("3_ex1")

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
np.where(part_digits)
# %%

part_nums = []

dig_x, dig_y = np.where(part_digits == True)
for x, y in zip(dig_x, dig_y):
    xmin = x
    xmax = x 
