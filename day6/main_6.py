# TODO improve perf
from copy import deepcopy

with open('input') as f:
    input_data = f.readlines()
input_data = [i.strip() for i in input_data]

start_position = [[i, input_data[i].index('^')] for i in range(len(input_data)) if "^" in input_data[i]][0]



def detect_loop_i(data_map, position, direction):
    i = position[0]
    j = position[1]
    loop = False
    exited = True
    new_position = position
    if direction == '^':
        for i, v in list(enumerate(data_map))[i::-1]:
            if (data_map[i][j].count('u')) > 0:
                loop = True
                break

            if v[j] == '#':
                new_position = [i+1, j]
                exited = False
                break
            else:
                if data_map[i][j] == '.':
                    data_map[i][j] = 'u'
                else:
                    data_map[i][j] = "".join(sorted(f"{data_map[i][j]}u"))

    elif direction == 'v':
        for i, v in list(enumerate(data_map))[i::1]:
            if (data_map[i][j].count('d')) > 0:
                loop = True
                break
            if v[j] == '#':
                new_position = [i-1, j]
                exited = False
                break
            else:
                if data_map[i][j] == '.':
                    data_map[i][j] = 'd'
                else:
                    data_map[i][j] = "".join(sorted(f"{data_map[i][j]}d"))
    elif direction == '>':
        for j, v in list(enumerate(data_map[i]))[j::1]:
            if (data_map[i][j].count('r')) > 0:
                loop = True
                break
            if v == '#':
                exited = False
                new_position = [i, j-1]
                break
            else:
                if data_map[i][j] == '.':
                    data_map[i][j] = 'r'
                else:
                    data_map[i][j] = "".join(sorted(f"{data_map[i][j]}r"))


    elif direction == '<':
        for j, v in list(enumerate(data_map[i]))[j::-1]:
            if data_map[i][j].count('l') > 0:
                loop = True
                break
            if v == '#':
                exited = False
                new_position = [i, j+1]
                break
            else:
                if data_map[i][j] == '.':
                    data_map[i][j] = 'l'
                else:
                    data_map[i][j] = "".join(sorted(f"{data_map[i][j]}l"))


    return data_map, exited, new_position, loop

def detect_loop(data_map, position, direction):
    loop = False
    exited = False
    rotation = direction
    while (not exited and not loop):
        #print('step', position, data_map[position[0]][ position[1]], rotation)
        data_map, exited, position, loop = detect_loop_i(data_map, position, rotation)
        rotation = rotate(rotation)
    return loop


def go_to_obstacle(data_map, position, direction):
    possible_loop_obstacles = []
    i = position[0]
    j = position[1]
    exited = True
    new_position = position
    obs_position = None
    if direction == '^':
        for i, v in list(enumerate(data_map))[i::-1]:
            if v[j] == '#':
                obs_position = [i, j]
                new_position = [i+1, j]
                exited = False
                break
            else:
                data_map[i][j] = 'X'
            #if len(list(filter(lambda visit: visit[0] == i and visit[1] > j, visited_obs))) > 0:
                #if 0 <= i - 1 < len(data_map) and data_map[i-1][j] != '#' and data_map[i+1][j] != 'X':
                    #print('poss loop', (i-1, j), list(filter(lambda visit: visit[0] == i and visit[1] > j, visited_obs)))
                    #possible_loop_obstacles.append((i - 1, j))

    elif direction == 'v':
        for i, v in list(enumerate(data_map))[i::1]:
            if v[j] == '#':
                obs_position = [i, j]
                new_position = [i-1, j]
                exited = False
                break
            else:
                data_map[i][j] = 'X'
            #if len(list(filter(lambda visit:  visit[0] == i and visit[1] < j, visited_obs))) > 0:
                #if 0 <= i + 1 < len(data_map) and data_map[i+1][j] != '#' and data_map[i+1][j] != 'X':
                    #print('poss loop', (i+1, j), list(filter(lambda visit: visit[0] == i and visit[1] < j, visited_obs)))
                    #possible_loop_obstacles.append((i + 1, j))

    elif direction == '>':
        for j, v in list(enumerate(data_map[i]))[j::1]:
            if v == '#':
                obs_position = [i, j]
                exited = False
                new_position = [i, j-1]
                break
            else:
                data_map[i][j] = 'X'
            #if len(list(filter(lambda visit:  visit[1] == j and visit[0] > i, visited_obs))) > 0:
                #if 0 <= j + 1 < len(data_map[0]) and data_map[i][j+1] != '#' and data_map[i][j+1] != 'X':
                    #print('poss loop', (i-1, j), list(filter(lambda visit: visit[0] == i and visit[1] > j, visited_obs)))
                    #possible_loop_obstacles.append((i , j + 1))
    elif direction == '<':
        for j, v in list(enumerate(data_map[i]))[j::-1]:
            if v == '#':
                obs_position = [i, j]
                exited = False
                new_position = [i, j+1]
                break
            else:
                data_map[i][j] = 'X'
            #if len(list(filter(lambda visit: visit[1] == j and visit[0] < i, visited_obs))) > 0:
                #if 0 <= j - 1 < len(data_map[0]) and data_map[i][j - 1] != '#' and data_map[i][j - 1] != 'X':
                    # print('poss loop', (i-1, j), list(filter(lambda visit: visit[0] == i and visit[1] > j, visited_obs)))
                    #possible_loop_obstacles.append((i, j - 1))
    return data_map, exited, new_position, obs_position, possible_loop_obstacles


exited = False

position = start_position
start_rotation = '^'
rotation = start_rotation
data_map = [[j for j in i] for i in input_data]
org_map = deepcopy(data_map)
def rotate(rotation):
    if rotation == '^':
        return '>'
    elif rotation == '>':
        return 'v'
    elif rotation == 'v':
        return '<'
    elif rotation == '<': return '^'

while not exited:
    data_map, exited, position, obst_posi, poss_loop = go_to_obstacle(data_map, position, rotation)
    rotation = rotate(rotation)

print(sum(["".join(i).count("X") for i in data_map]))
#print(start_position)

loops = set()
for i in range(len(org_map)):
    for j in range(len(org_map)):
        #i, j = (5,36)
        print("scan", i, j, len(loops))
        new_map = deepcopy(org_map)
        if new_map[i][j] == '.':
            new_map[i][j] = '#'
            if detect_loop(new_map, start_position, start_rotation):
                loops.add((i,j,))
print(len(loops))



