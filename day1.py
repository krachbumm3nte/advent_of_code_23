import utils
import re

lines = utils.readlines("1")

values = []

# for l in lines:
#     vals = re.findall("\d", l)
#     if len(vals) == 1:
#         num = int(vals[0] + vals[0])
#     else:
#         num = int(vals[0] + vals[-1])
#     values.append(num)

# print(sum(values))


values = []


digit_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


for line in lines:
    
    vals = []
    
    for i in range(len(line)):
        if hit := re.match(r"(\d|one|two|three|four|five|six|seven|eight|nine)", line[i:]):
            hit = hit.groups()[0]
            if len(hit) != 1:
                hit = digit_dict[hit]
            vals.append(hit)
    
    if len(vals) == 1:
        num = int(vals[0] + vals[0])
    else:
        num = int(vals[0] + vals[-1])
    values.append(num)
    print(line, vals, num)

print(sum(values))
