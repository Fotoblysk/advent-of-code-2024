import functools
# read input
input_data = None
with open('input') as f:
    input_data = f.readlines()
data_set = [[], []]

# split to 2 list
for line in input_data:
    for j, cell in enumerate(filter(lambda el: el != '', line.strip().split(' '))):
        data_set[j].append(int(cell.strip()))

for j in range(len(data_set)):
    data_set[j] = sorted(data_set[j])

def distance(a, b):
    return abs(a-b)

distances = [ distance(data_set[0][i], data_set[1][i]) for i, v in enumerate(data_set[0]) ]
print(sum(distances))

uniq_ids = set(data_set[0])
occurrences_in_second_set = {i: 0 for i in uniq_ids}

for i in data_set[1]:
    if i in occurrences_in_second_set:
        occurrences_in_second_set[i] += 1


strange_sum = sum(map(lambda curr_id: curr_id*occurrences_in_second_set[curr_id] if curr_id in occurrences_in_second_set else 0, data_set[0]))
print(strange_sum)

occurrences_in_second_set.items()