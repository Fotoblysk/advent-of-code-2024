import functools
import re

# read input
input_data = None
with open('input') as f:
    input_data = f.readlines()
input_data = [i.strip() for i in input_data]
print(input_data)

limits = {"red":12 , "green":13 , "blue": 14}
blues = [ for line in input_data]

