import functools
import re

# read input
input_data = None
with open('input') as f:
    input_data = f.readlines()
input_data = [i.strip() for i in input_data]
# print(input_data)

#results_per_line = [re.findall(r'\d', line) for line in input_data]
#results = [int(str(rl[0]) + str(rl[-1])) for rl in results_per_line]
#print(sum(results))

mapping_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

results_per_line = [list(re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)) for line in
                    input_data]

print(results_per_line)

results = [int(str(mapping_dict[rl[0]] if rl[0] in mapping_dict else rl[0]) + str(
    mapping_dict[rl[-1]] if rl[-1] in mapping_dict else rl[-1])) for rl in results_per_line]
print(sum(results))

import regex
test = "1234"
print(list(regex.findall(r'\d+', test, overlapped=True))) # that also sucks


