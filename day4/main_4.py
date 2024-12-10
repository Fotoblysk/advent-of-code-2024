# read input
import re
from array import array
from enum import Enum
from tkinter.constants import HORIZONTAL, NORMAL, VERTICAL


class DirectionVariant(Enum):
    HORIZONTAL = 1
    VERTICAL = 2
    LEFT_TO_BOTTOM = 3
    RIGHT_TO_BOTTOM = 4

class OrderVariant(Enum):
    NORMAL = 1
    BACKWARDS = 3


def find_xmas_occ_n(searched_string_arr, search_string=r'XMAS', middle_only=False):
    if not middle_only:
        return sum( [len([i.start(0) for i in re.finditer(search_string, searched_string)]) for searched_string in searched_string_arr])
    else:
        return sum( [len([i.start(0) for i in re.finditer(search_string, searched_string)]) for searched_string in searched_string_arr[len(searched_string_arr)//2:len(searched_string_arr)//2+1]])

def get_string_array(variant: (DirectionVariant, OrderVariant), org_string):
    if variant[1] == OrderVariant.NORMAL:
        order_fn = lambda a: a
    else:
        order_fn = lambda a: [i[::-1] for i in a]

    if variant[0] == DirectionVariant.HORIZONTAL:
        return order_fn(org_string)
    elif variant[0] == DirectionVariant.VERTICAL:
        new_array = [[org_string[j][i] for j in range(len(org_string))] for i in range(len(org_string[0]))]
        new_array = ["".join(new_array[j]) for j in range(len(new_array))]
        return order_fn(new_array)
    elif variant[0] == DirectionVariant.LEFT_TO_BOTTOM:
        new_array = []
        #test_array = ['abc',
        #              'def',
        #              'ghi']
        #org_string = test_array
        for j in reversed(range(len(org_string[0]))):
            new_array.append([])
            for p in range(len(org_string[0]) - j):
                new_array[-1].append(org_string[p][j+p])

        for j in list(range(len(org_string)))[1:]:
            new_array.append([])
            for p in range(len(org_string) - j):
                new_array[-1].append(org_string[j+p][p])
        new_array = ["".join(i) for i in new_array]
        return order_fn(new_array)

    elif variant[0] == DirectionVariant.RIGHT_TO_BOTTOM:
        new_array = []
        org_string_rev = [i[::-1] for i in org_string]
        for j in reversed(range(len(org_string_rev[0]))):
            new_array.append([])
            for p in range(len(org_string_rev[0]) - j):
                new_array[-1].append(org_string_rev[p][j+p])

        for j in list(range(len(org_string_rev)))[1:]:
            new_array.append([])
            for p in range(len(org_string_rev) - j):
                new_array[-1].append(org_string_rev[j+p][p])
        new_array = ["".join(i) for i in new_array]
        return order_fn(new_array)


input_data = None
with open('input') as f:
    input_data = f.readlines()
input_data = [i.strip() for i in input_data]
total_occ = sum([find_xmas_occ_n(get_string_array((direction, order), input_data)) for direction in [DirectionVariant.VERTICAL, DirectionVariant.HORIZONTAL, DirectionVariant.LEFT_TO_BOTTOM, DirectionVariant.RIGHT_TO_BOTTOM]
                 for order in [OrderVariant.NORMAL, OrderVariant.BACKWARDS]])
print(total_occ)
total_occ = 0
for i in range(len(input_data[:-2])):
    for j in range(len(input_data[i][:-2])):
        sliced_input_data = []
        for z in range(3):
            sliced_input_data.append(input_data[i+z][j:j+3])
        occ = sum([find_xmas_occ_n(get_string_array((direction, order), sliced_input_data), search_string='MAS', middle_only=True) for direction in [DirectionVariant.LEFT_TO_BOTTOM, DirectionVariant.RIGHT_TO_BOTTOM]
                         for order in [OrderVariant.NORMAL, OrderVariant.BACKWARDS]])
        total_occ = total_occ + 1  if occ >= 2 else total_occ
        #total_occ += occ // 2
print(total_occ)