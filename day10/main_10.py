# TODO improve perf
from copy import deepcopy
import itertools
from inspect import trace

with open('input') as f:
    input_data = f.readlines()
input_data = [i.strip() for i in input_data]
[print(i) for i in input_data]
input_data = [[int(j) for j in i] for i in input_data]
#print(input_data)

def find_trails_r(data, last_point):
    traces = []
    i, j = last_point
    up, down, left, right = (i-1, j), (i+1, j),(i, j-1), (i, j+1)
    directions = [up, down, left, right]
    directions = [dirz for dirz in directions if 0<=dirz[0]<len(data) and 0<=dirz[1]<len(data[0])]
    for new_point in directions:
        if data[new_point[0]][new_point[1]] == data[last_point[0]][last_point[1]] + 1:
            if data[new_point[0]][new_point[1]] != 9:
                #print("ft", data, new_point)
                next_traces = find_trails_r(data, new_point)
                for t in next_traces:
                    new_trace = [new_point]
                    #print("t", t)
                    new_trace.extend(t)
                    traces.append(new_trace)
            else:
                traces.append([new_point])
    #print("r", traces)
    return traces


def find_trails(data):
    zeros = [(i,j) for i in range(len(data)) for j in range(len(data[i])) if data[i][j] == 0]
    trails = dict()
    #print(zeros)
    for z in zeros:
        trails[z] = find_trails_r(data, z)
    return trails

found_trails = find_trails(input_data)
[print(i, v) for i, v in found_trails.items()]

def get_trails_sum(trails):
    zeros_sum = dict()
    for z in trails:
        finish_points = set()
        for t in trails[z]:
            if t[-1] not in finish_points:
                finish_points.add(t[-1])
        zeros_sum[z] = len(finish_points)
    return zeros_sum

def get_rating_sum(trails):
    zeros_sum = dict()
    for z in trails:
        zeros_sum[z] = len(trails[z])
    return zeros_sum

trails_sum = get_trails_sum(found_trails)
print(get_trails_sum(found_trails))
print(sum(trails_sum.values()))

print(sum(get_rating_sum(found_trails).values()))