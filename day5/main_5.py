
input_data = None
with open('input') as f:
    input_data = f.readlines()
input_data = [i.strip() for i in input_data]


#input_data = """47|53
#97|13
#97|61
#97|47
#75|29
#61|13
#75|53
#29|13
#97|29
#53|29
#61|53
#97|53
#61|29
#47|13
#75|47
#97|75
#47|61
#75|61
#47|29
#75|13
#53|13
#_
#75,47,61,53,29
#97,61,53,29,13
#75,29,13
#75,97,47,61,53
#61,13,29
#97,13,75,29,47""".split("\n")
#input_data[21] = ""
print(input_data[-1])

empty_index = [i for i, v in enumerate(input_data) if v == ''][0]

rules, updates = input_data[0:empty_index], input_data[empty_index+1:]
updates = [i.split(',') for i in updates]
updates = [[int(j) for j in i] for i in updates]


# rename to forward
rules_forward_list = [[int(i.split('|')[0]), int(i.split('|')[1])] for i in rules]

all_uniqe = set()
for i in rules_forward_list:
    all_uniqe.add(i[0])
    all_uniqe.add(i[1])


rules_forward = dict()
for i in rules_forward_list:
    if i[0] in rules_forward:
        rules_forward[i[0]].append(i[1])
    else:
        rules_forward[i[0]] = [i[1]]

rules_backward = dict()
for i in rules_forward_list:
    if i[1] in rules_backward:
        rules_backward[i[1]].append(i[0])
    else:
        rules_backward[i[1]] = [i[0]]

def get_absolute_order_list(update, rules_backward):
    absolute_order = []
    set_update = set(update) # probably not needed for smaller lists
    used_rules_backward = {k: list(filter(lambda i: i in set_update, v)) for k, v in rules_backward.items() if k in set_update}
    used_rules_backward = {k: v for k, v in used_rules_backward.items() if len(v) > 0 }
    while len(set_update) > 0:
        diff = set_update.difference(used_rules_backward.keys())
        if len(diff) > 0: # can be inf loop
            absolute_order.append(diff)
        set_update = set_update.difference(diff)
        used_rules_backward = {k: list(filter(lambda i: i in set_update, v)) for k, v in used_rules_backward.items() if k in set_update}
        used_rules_backward = {k: v for k, v in used_rules_backward.items() if len(v) > 0 }
    return absolute_order

def check_order(update, rules_forward):
    set_update = set(update) # probably not needed for smaller lists
    used_rules_forward = {k: list(filter(lambda i: i in set_update, v)) for k, v in rules_forward.items() if k in set_update}
    used_rules_forward = {k: v for k, v in used_rules_forward.items() if len(v) > 0 }

    passed_items = set()
    for i, v in enumerate(update):
        passed_items.add(v)
        if v in used_rules_forward:
            for should_be_after in used_rules_forward[v]:
                if should_be_after in passed_items:
                    return False
    return True

def get_middle_item(update):
    return update[len(update)//2]

def correct_order(uncorrected_list, abs_order):
    new_list = []
    abs_index = 0
    while len(new_list) != len(uncorrected_list):
        for i in uncorrected_list:
            if i in abs_order[abs_index]:
                abs_order[abs_index].remove(i)
                new_list.append(i)
                if len(abs_order[abs_index]) == 0:
                    abs_index += 1
                    break
    return new_list


print(sum([get_middle_item(update) for update in updates if check_order(update, rules_forward)]))

#print(updates[-1])

#print([[correct_order(update, get_absolute_order_list(update, rules_backward)), update] for update in updates if not check_order(update, rules_forward)])

print(sum([get_middle_item(correct_order(update, get_absolute_order_list(update, rules_backward))) for update in updates if not check_order(update, rules_forward)]))






