# TODO improve perf
from copy import deepcopy
import itertools

with open('input') as f:
    input_data = f.readlines()
input_data = [i.strip() for i in input_data]
[print(i) for i in input_data]


def get_symbols(input_data):
    symbols = set([j for i in input_data for j in i])
    symbols.remove(".")
    return symbols


def get_symbol_positions(input_data, symbols):
    symbol_positions = dict()
    for s in symbols:
        symbol_positions[s] = []
        for i in range(len(input_data)):
            for j, v in enumerate(input_data[i]):
                if v == s:
                    symbol_positions[s].append((i, j,))
    return symbol_positions


symbols = get_symbols(input_data)
#print(symbols)
sym_pos = get_symbol_positions(input_data, symbols)
#print(sym_pos)


def get_dist(a, b):
    return (a[0] - b[0]), a[1] - b[1]

def scal_prod(scal, vec):
    return scal*vec[0], scal*vec[1]



def get_sym_node_pos(data, pos, check_dist):
    perms = list(itertools.permutations(pos, 2))
    nodes_pos = []
    for a, b in perms:  # much of not needed checks
        for i in range(len(data)):
            for j in range(len(data[i])):
                # a, b , (i, j)
                dist_a = get_dist(a, (i, j))
                dist_b = get_dist(b, (i, j))
                vec_ab = get_dist(a, b)
                vec_ac = get_dist(b, (i, j))
                if check_dist:
                    if (scal_prod(2,dist_a) == dist_b or scal_prod(2,dist_b) == dist_a) and ((vec_ab[1] == 0 and vec_ac[1] == 0) or (vec_ab[1] != 0 and vec_ac[1] != 0 and vec_ab[0]/vec_ab[1] == vec_ac[0]/vec_ac[1])):
                        #print('found')
                        #print(i, j, a, b, dist_a, dist_b)
                        nodes_pos.append((i, j))
                else:
                    if (vec_ab[1] != 0 and vec_ac[1] != 0 and vec_ab[0]/vec_ab[1] == vec_ac[0]/vec_ac[1]):
                        nodes_pos.append((i, j))

    return nodes_pos


def get_nodes(data, sym_pos, check_dist=True):
    nodes_pos = deepcopy(data)
    nodes_pos = [['.' for j in i] for i in nodes_pos]
    for s in sym_pos:
        new_pos = get_sym_node_pos(data, sym_pos[s], check_dist)
        for x_pos, y_pos in new_pos:
            nodes_pos[x_pos][y_pos] = "#"

    return nodes_pos


print(len([j for i in get_nodes(input_data, sym_pos) for j in i if j == "#"]))

[print("".join(i)) for i in get_nodes(input_data, sym_pos, check_dist=False)]
print(len([j for i in get_nodes(input_data, sym_pos, check_dist=False) for j in i if j == "#"]))
