# TODO improve perf
from copy import deepcopy
import itertools

with open('input') as f:
    input_data = f.readlines()
input_data = [i.strip() for i in input_data]
input_data = input_data[0]

def encode_input(data):
    encoded_in = []
    for i, v in enumerate(data):
        id_ = i//2
        is_block = (i%2) == 0
        if is_block:
            encoded_in.extend([str(id_)]*int(v))
        else:
            encoded_in.extend(["."]*int(v))
    return encoded_in


enc_data = encode_input(input_data)
#print(enc_data)

def comp_encoded(data):
    dot_indices = [i for i, v in enumerate(data) if v == '.']
    list_data = [i for i in data]
    last_j = len(list_data)
    for t, i in enumerate(dot_indices):
        #print(t, len(dot_indices))
        for j, v in reversed(list(enumerate(list_data[:last_j]))):
            if j > i and v != ".":
                last_j = j
                list_data[i] = v
                list_data[j] = "."
                break

    return list_data

def find_blocks(list_d):
    blocks = []
    prev_list_v = -2
    for i, v in enumerate(list_d):
        if v != prev_list_v:
            blocks.append((i,i+1))
            prev_list_v = v
        else:
            blocks[-1] = (blocks[-1][0], i+1)
    file_blocks = [(s,e) for s, e in blocks if list_d[s] != '.']
    dot_blocks = [(s,e) for s, e in blocks if list_d[s] == '.']
    return file_blocks, dot_blocks


def comp_encoded_blocks(data):
    list_data = [i for i in data]
    file_blocks, _ = find_blocks(list_data)
    for t, (start, end) in enumerate(reversed(file_blocks)):
        #print(t, len(file_blocks))
        _, dot_blocks = find_blocks(list_data)
        for d_start, d_end in dot_blocks:
            if d_end-d_start >= end - start:
                if start>d_start:
                    for i in range(start, end):
                        list_data[d_start+i-start] = list_data[i]
                        list_data[i] = "."

    return list_data

def calc_check(data):
    return sum([int(i)*int(v) for i,v in enumerate(data) if v != "."])

#res = comp_encoded(enc_data)
#print(res)
#print(calc_check(res))
print(calc_check(comp_encoded_blocks(enc_data)))