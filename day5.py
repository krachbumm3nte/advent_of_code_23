# %%

import utils
import re
import numpy as np


content = utils.readstring("5")
lines = content.split("\n\n")

seeds = lines[0]
lines = lines[1:]

seeds = seeds.split(":")[1].strip()
seeds = re.split("\ +", seeds)
seeds = [int(i) for i in seeds]


maps = [l.split(":")[1].strip() for l in lines]
# maps = [[submap.split(" ") for submap in m.split("\n")] for m in maps]

maps_formatted = []
for m in maps:
    print(m)
    partial_maps = m.split("\n")
    map_fmt = []
    for part in partial_maps:
        part = part.split(" ")
        part = [int(v) for v in part]
        map_fmt.append(part)
    maps_formatted.append(map_fmt)

maps = maps_formatted
# %%

location_nums = []

for s in seeds:
    source = s
    for m in maps:
        for dest_start, source_start, map_len in m:
            if source_start <= source <= source_start + map_len:
                source = dest_start + source - source_start
                break
    location_nums.append(source)
# %%
print(min(location_nums))
# %%


def process_seedrange(orig_start, orig_len, maps):
    # print(orig_start, orig_len, len(maps))
    if len(maps) == 0:
        return orig_start

    orig_end = orig_start + orig_len
    for submap in maps[0]:
        dest_start, map_start, map_len = submap
        map_end = map_start + map_len
        if map_start <= orig_start:
            if map_end <= orig_start:
                continue
            mapped_start = dest_start + orig_start - map_start
            if orig_end <= map_start + map_len:
                return process_seedrange(mapped_start, orig_len, maps[1:])
            elif orig_start <= map_end:
                new_len_0 = map_end - orig_start
                new_len_1 = orig_len - new_len_0

                result_0 = process_seedrange(mapped_start, new_len_0, maps[1:])
                result_1 = process_seedrange(map_end, new_len_1, maps)
                return min(result_0, result_1)
        else:  # map_start > orig_start
            if map_start >= orig_end:
                continue
            if map_end > orig_end:
                new_len_0 = map_start - orig_start
                new_len_1 = orig_end - map_start

                result_0 = process_seedrange(orig_start, new_len_0, maps)
                result_1 = process_seedrange(dest_start, new_len_1, maps[1:])
                return min(result_0, result_1)
            else:
                new_len_0 = map_start - orig_start
                new_len_1 = map_len
                new_len_2 = orig_end - map_end

                result_0 = process_seedrange(orig_start, new_len_0, maps)
                result_1 = process_seedrange(dest_start, new_len_1, maps[1:])
                result_2 = process_seedrange(map_end, new_len_2, maps)
                return min(result_0, result_1, result_2)
    else:
        return process_seedrange(orig_start, orig_len, maps[1:])


results = []

for i in range(len(seeds) // 2):
    s = seeds[2 * i]
    r = seeds[2 * i + 1]
    results.append(process_seedrange(s, r, maps))

print(min(results))

# %%
