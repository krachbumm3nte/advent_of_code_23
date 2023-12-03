import os

def readlines(idx: int):
    
    with open(os.path.join("inputs", f"input_{idx}.txt")) as f:
        lines = f.readlines()
    return [l.strip("\n") for l in lines]