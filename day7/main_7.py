# TODO improve perf
from copy import deepcopy
import itertools

with open('input') as f:
    input_data = f.readlines()
input_data = [i.strip() for i in input_data]


def preprocess_input(input_d):
    pre_input_d = [(int(i.split(':')[0]), [int(j) for j in i.split(':')[1].strip().split(' ')]) for i in input_data]
    return pre_input_d


def generate_operation_perms(elems, signs):
    perms = list(itertools.product(signs, repeat=len(elems) - 1))
    #print(perms)
    return perms


def test_eq(elems, operations, ex_result):
    result = elems[0]
    for i, op in enumerate(operations):
        if op == "*":
            result *= elems[i + 1]
        elif op == "+":
            result += elems[i + 1]
        elif op == "||":
            result = int(str(result) + str(elems[i+1]))


    return ex_result == result


def find_possible_combinations(parsed_input, signs):
    possible_comb = []
    for ex_result, elems in parsed_input:
        possible_comb.append(set())
        operations_perm = generate_operation_perms(elems, signs)
        for operations in operations_perm:
            if test_eq(elems, operations, ex_result):
                possible_comb[-1].add(operations)
    return possible_comb




parsed_input = preprocess_input(input_data)
#print(parsed_input)

possible_comb = find_possible_combinations(parsed_input, ["+", "*"])
sum_of_possible_test = sum( [parsed_input[i][0] for i,v in enumerate(possible_comb) if len(v)>0])
print(sum_of_possible_test)

possible_comb = find_possible_combinations(parsed_input, ["+", "*", "||"])
sum_of_possible_test = sum( [parsed_input[i][0] for i,v in enumerate(possible_comb) if len(v)>0])
print(sum_of_possible_test)
