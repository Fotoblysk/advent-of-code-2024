# TODO improve perf
import itertools
from copy import deepcopy
from inspect import trace

# {number: [{times: value}]}
cache = dict()

with open('input') as f:
    input_data = f.readlines()
input_data = [i.strip() for i in input_data]
#[print(i) for i in input_data]
input_data = [int(i) for i in input_data[0].split()]
#print(input_data)

def aplay_single_digit_rules(num):
    str_num = str(num)
    len_str_num = len(str(num))
    if num == 0:
        return [1]
    elif len_str_num % 2 == 0:
        half_len_str_num = len_str_num//2
        return [int(str_num[0:half_len_str_num]), int(str_num[half_len_str_num:])]
    else:
        return [2024*num]

def aplay_rules(data):
    new_data = []
    for i in data:
        new_data.extend(aplay_single_digit_rules(i))
    return new_data

def blink_n_times(data, n):
    new_data = deepcopy(list(data))
    for i in range(n):
        new_data = aplay_rules(new_data)
    return new_data

def aplay_rule_n(num, n):
    if n == 0:
        return 1

    single_res = aplay_single_digit_rules(num)
    lens = 0
    for i in single_res:
        if (i, n-1) in cache:
            tmp_len = cache[(i, n-1)]
        else:
            tmp_len = aplay_rule_n(i, n-1)
        lens += tmp_len
        if (i, n-1) not in cache:
            cache[(i, n-1)] = tmp_len

    return lens



def dp_blink_n_times(data, n):
    new_data = []
    for num in data:
        new_num = aplay_rule_n(num, n)
        new_data.append(new_num)
    return sum(new_data)


print(len(blink_n_times(input_data, 25)))
print(dp_blink_n_times(input_data, 75))
