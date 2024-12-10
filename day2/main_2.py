def anal_report(report, inc, max_num_of_unsafe, num_of_unsafe=0):
    if num_of_unsafe > max_num_of_unsafe:
        return False
    for i in range(len(report[:-1])):
        v1, v2 = report[i], report[i + 1]
        if inc and v2 - v1 > 0 or not inc and v2 - v1 < 0:
            if 1 <= abs(v2 - v1) <= 3:
                pass
            else:
                num_of_unsafe += 1
                return anal_report([*report[0:i], *report[i + 1:]], inc,  max_num_of_unsafe, num_of_unsafe) or anal_report(
                    [*report[0:i + 1], *report[i + 2:]], inc, max_num_of_unsafe, num_of_unsafe)
        else:
            num_of_unsafe += 1
            return anal_report([*report[0:i], *report[i + 1:]], inc, max_num_of_unsafe, num_of_unsafe) or anal_report(
                [*report[0:i + 1], *report[i + 2:]], inc, max_num_of_unsafe, num_of_unsafe)
    return True


def is_report_safe(report, max_num_of_unsafe=0):
    # assume inc
    return anal_report(report, True, max_num_of_unsafe) or anal_report(report, False, max_num_of_unsafe)


import functools

# read input
input_data = None
with open('input') as f:
    input_data = f.readlines()
data_set = []

# split to 2 list
for line in input_data:
    data_set.append([])
    for cell in filter(lambda el: el != '', line.strip().split(' ')):
        data_set[-1].append(int(cell.strip()))
reports = data_set

safe_reports_n = len(list(filter(lambda a: is_report_safe(a), reports)))
print(safe_reports_n)
safe_reports_n_1_wrong = len(list(filter(lambda a: is_report_safe(a, 1), reports)))
print(safe_reports_n_1_wrong)
