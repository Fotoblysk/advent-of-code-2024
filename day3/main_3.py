# read input
import re


def calc_result(func_input):
    res = re.findall(r'mul\(([0-9]+),([0-9]+)\)', func_input)
    prod_sum = 0
    for n1, n2 in res:
        prod_sum += int(n1) * int(n2)
    print(prod_sum)


input_data = None
with open('input') as f:
    input_data = f.readlines()
input_data = "".join(input_data)

calc_result(input_data)

res = re.finditer(r"(do\(\)|don't\(\))", input_data)
enabled_string = ''

disabled = False
removed_indices = []

for i in res:
    if i.group() == 'do()':
        if disabled and len(removed_indices) > 0:
            removed_indices[-1].append(i.start(0))
        disabled = False
    if i.group() == "don't()":
        if not disabled:
            removed_indices.append([i.end(0)])
        disabled = True

fixed_input = input_data
for i in reversed(removed_indices):
    start_phrase_index = -1
    end_phrase_index = i[0]
    if len(i) > 1:
        #print('start')
        start_phrase_index = i[1]
    fixed_input = f"{fixed_input[0:end_phrase_index]}{fixed_input[start_phrase_index:-1]}"

calc_result(fixed_input)
