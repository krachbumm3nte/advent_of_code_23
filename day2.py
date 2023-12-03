import utils
import re
import numpy as np

lines = utils.readlines("2")


possible_games = []

max_vals = {"red": 12, "green": 13, "blue": 14}


for l in lines:
    game_no, sets = l.split(":")
    game_no = int(game_no.split(" ")[1])

    sets = sets.split(";")

    possible = True
    for set in sets:
        if not possible:
            break
        dice = set.split(",")
        for die in dice:
            num, col = die.strip().split(" ")
            if int(num) > max_vals[col]:
                possible = False
                break
    if possible:
        possible_games.append(int(game_no))

print(sum(possible_games))


power_sum = 0

for l in lines:
    game_no, sets = l.split(":")
    game_no = int(game_no.split(" ")[1])

    sets = sets.split(";")

    max_vals = {"red": 0, "green": 0, "blue": 0}


    for set in sets:
        dice = set.split(",")
        for die in dice:
            num, col = die.strip().split(" ")
            if int(num) > max_vals[col]:
                max_vals[col] = int(num)
    
    power_sum += np.prod(list(max_vals.values()))
  
print(power_sum)