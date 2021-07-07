# [(passed, total_time, points, judge_seq),(cp, split, sum of previous splits), ...]
def calculate_classic(seq, times, control_seq, comp_type):
    # prepare strings into list
    if times[-1] == '-':
        times = times[:-1]
    if times[0] == '-':
        times = times[1:]
    times = times.split("-")
    if seq[-1] == '-':
        seq = seq[:-1]
    if seq[0] == '-':
        seq = seq[1:]
    seq = seq.split("-")
    if control_seq[-1] == '-':
        control_seq = control_seq[:-1]
    if control_seq[0] == '-':
        control_seq = control_seq[1:]
    control_seq = control_seq.split("-")
    # extra output variables
    passed = False
    judge_seq = []
    result = []
    points = 0
    total_time = 0
    # end of check
    if comp_type == 1:
        index = -1
        temp_seq = seq
        for i in control_seq:
            if str(i) not in temp_seq:
                break
            else:
                for j in temp_seq:
                    if i == j:
                        if temp_seq.index(j) > index:
                            result.append((i, temp_seq.index(j)))
                            index = temp_seq.index(j)
                            for o in range(0, index):
                                temp_seq[o] = '.' + temp_seq[o]
                            temp_seq[temp_seq.index(j)] = '|' + str(j) + '|'
                            break
        # cleanup
        for p in temp_seq:
            temp_seq[temp_seq.index(p)] = p.replace('.', '')
        judge_seq = temp_seq
        # total time
        for sec in times:
            total_time += int(sec)
        # points
        for res in result:
            if int(res[0]) > 30:
                points += int(res[0]) // 10
        if not result:
            temp_seq = [(None, None, None)]
            result = [(None, None, None)]
        else:

            ##############################

            # time process
            delta = 0
            for i in range(len(result)):
                split = 0
                if i < int(len(result) - 1):
                    tmp = result[i]
                    tmp_ = result[i + 1]
                    if tmp_[1] - tmp[1] > 1:
                        for k in range(tmp_[1] - tmp[1]):
                            split += int(times[i + k + delta])
                        result[i] = (tmp[0], split)
                        delta += tmp_[1] - tmp[1] - 1
                    else:
                        split += int(times[delta + i])
                        result[i] = (tmp[0], split)
                else:
                    tmp = result[i]
                    tmp_ = int(len(times))
                    if tmp_ - tmp[1] > 1:
                        for k in range(tmp_ - tmp[1]):
                            split += int(times[i + k + delta])
                        result[i] = (tmp[0], split)
                        delta += tmp_ - tmp[1] - 1
                    else:
                        split += int(times[delta + i])
                        result[i] = (tmp[0], split)

        ##############################

        # sum of splits
        for j in range(len(result)):
            tmp = result[j]
            if j > 0:
                tmp_ = result[j - 1]
                result[j] = (tmp[0], tmp[1], tmp_[2] + tmp[1])
            else:
                result[j] = (tmp[0], tmp[1], tmp[1])
        check = result[0]
        if check[0] != None and check[1] != None:
            if len(result) == len(control_seq):
                passed = True
            else:
                passed = False
        else:
            passed = False
        for cp in judge_seq:
            if '|' in cp:
                judge_seq[temp_seq.index(cp)] = '<span class="approved">' + cp.replace('|', '') + '</span>'
            else:
                judge_seq[temp_seq.index(cp)] = '<span class="skip">' + cp + '</span>'

        service_tup = (passed, total_time, points, judge_seq)
        return [service_tup] + result
    elif comp_type == 2:
        passed = True
        # total time
        for sec in times:
            total_time += int(sec)
        # points
        for res in seq:
            if int(res) > 30:
                points += int(res) // 10
        for cp in seq:
            judge_seq.append('<span class="approved">' + cp + '</span>')
        for res in seq:
            result.append((res, int(times[seq.index(res)]), 999))

        service_tup = (passed, total_time, points, judge_seq)
        return [service_tup] + result


seq = '-27-31-51-62-30-'
times = '-00-1-2-3-4-'
control_seq = '-27-31-30'
comp_type = 2

print(calculate_classic(seq, times, control_seq, 2))
print('\n')
print(calculate_classic(seq, times, control_seq, 1))



# # [(passed, total_time, points, judge_seq),(cp, split, sum of previous splits), ...]
# def calculate_classic(seq, times, control_seq):
#     if times[-1] == '-':
#         times = times[:-1]
#     if times[0] == '-':
#         times = times[1:]
#     times = times.split('-')
#     if seq[-1] == '-':
#         seq = seq[:-1]
#     if seq[0] == '-':
#         seq = seq[1:]
#     seq = seq.split('-')
#     if control_seq[-1] == '-':
#         control_seq = control_seq[:-1]
#     if control_seq[0] == '-':
#         control_seq = control_seq[1:]
#     control_seq = control_seq.split('-')
#     # End of check
#     result = []
#     index = -1
#     temp_seq = seq
#
#     for i in control_seq:
#         if str(i) not in temp_seq:
#             break
#         else:
#             for j in temp_seq:
#                 if i == j:
#                     if temp_seq.index(j) > index:
#                         result.append((i, temp_seq.index(j)))
#                         index = temp_seq.index(j)
#                         for o in range(0, index):
#                             temp_seq[o] = '.' + temp_seq[o]
#                         temp_seq[temp_seq.index(j)] = '|' + str(j) + '|'
#                         break
#     # Cleanup
#     judge_seq=[]
#     for p in temp_seq:
#         temp_seq[temp_seq.index(p)] = p.replace('.', '')
#     judge_seq = temp_seq
#     # Total time
#     total_time = 0
#     for sec in times:
#         total_time += int(sec)
#     # Points
#     points = 0
#     for res in result:
#         if int(res[0]) > 30:
#             points += int(res[0]) // 10
#     if not result:
#         temp_seq = [(None, None, None)]
#         result = [(None, None, None)]
#     else:
#         # Time process
#         delta = 0
#         for i in range(len(result)):
#             split = 0
#             if i < int(len(result) - 1):
#                 tmp = result[i]
#                 tmp_ = result[i + 1]
#                 if tmp_[1] - tmp[1] > 1:
#                     for k in range(tmp_[1] - tmp[1]):
#                         split += int(times[i + k + delta])
#                     result[i] = (tmp[0], split)
#                     delta += tmp_[1] - tmp[1] - 1
#                 else:
#                     split += int(times[delta + i])
#                     result[i] = (tmp[0], split)
#             else:
#                 tmp = result[i]
#                 tmp_ = int(len(times))
#                 if tmp_ - tmp[1] > 1:
#                     for k in range(tmp_ - tmp[1]):
#                         split += int(times[i + k + delta])
#                     result[i] = (tmp[0], split)
#                     delta += tmp_ - tmp[1] - 1
#                 else:
#                     split += int(times[delta + i])
#                     result[i] = (tmp[0], split)
#     # Sum of splits
#     for j in range(len(result)):
#         tmp = result[j]
#         if j > 0:
#             tmp_ = result[j - 1]
#             result[j] = (tmp[0], tmp[1], tmp_[2] + tmp[1])
#         else:
#             result[j] = (tmp[0], tmp[1], tmp[1])
#     check = result[0]
#     if check[0] is not None and check[1] is not None:
#         if len(result) == len(control_seq):
#             passed = True
#         else:
#             passed = False
#     else:
#         passed = False
#     for cp in judge_seq:
#         if '|' in cp:
#             judge_seq[temp_seq.index(cp)] = '<span class="approved">' + cp.replace('|', '') + '</span>'
#         else:
#             judge_seq[temp_seq.index(cp)] = '<span class="skip">' + cp + '</span>'
#
#
#     service_tup = (passed, total_time, points, +judge_seq)
#     return [service_tup] + result

#[(passed, total_time, points, judge_seq), (cp, split, sum of previous splits), ...]


def calculate_classic(seq, times, control_seq, comp_type):
    if times[-1] == '-':
        times = times[:-1]
    if times[0] == '-':
        times = times[1:]
    times = times.split('-')
    if seq[-1] == '-':
        seq = seq[:-1]
    if seq[0] == '-':
        seq = seq[1:]
    seq = seq.split('-')
    if control_seq[-1] == '-':
        control_seq = control_seq[:-1]
    if control_seq[0] == '-':
        control_seq = control_seq[1:]
    control_seq = control_seq.split('-')
    # End of check
    if comp_type == 1:
        result = []
        index = -1
        temp_seq = seq

        for i in control_seq:
            if str(i) not in temp_seq:
                break
            else:
                for j in temp_seq:
                    if i == j:
                        if temp_seq.index(j) > index:
                            result.append((i, temp_seq.index(j)))
                            index = temp_seq.index(j)
                            for o in range(0, index):
                                temp_seq[o] = '.' + temp_seq[o]
                            temp_seq[temp_seq.index(j)] = '|' + str(j) + '|'
                            break
        # Cleanup
        judge_seq = []
        for p in temp_seq:
            temp_seq[temp_seq.index(p)] = p.replace('.', '')
        judge_seq = temp_seq
        # Total time
        total_time = 0
        for sec in times:
            total_time += int(sec)
        # Points
        points = 0
        for res in result:
            if int(res[0]) > 30:
                points += int(res[0]) // 10
        if not result:
            temp_seq = [(None, None, None)]
            result = [(None, None, None)]
        else:
            # Time process
            delta = 0
            for i in range(len(result)):
                split = 0
                if i < int(len(result) - 1):
                    tmp = result[i]
                    tmp_ = result[i + 1]
                    if tmp_[1] - tmp[1] > 1:
                        for k in range(tmp_[1] - tmp[1]):
                            split += int(times[i + k + delta])
                        result[i] = (tmp[0], split)
                        delta += tmp_[1] - tmp[1] - 1
                    else:
                        split += int(times[delta + i])
                        result[i] = (tmp[0], split)
                else:
                    tmp = result[i]
                    tmp_ = int(len(times))
                    if tmp_ - tmp[1] > 1:
                        for k in range(tmp_ - tmp[1]):
                            split += int(times[i + k + delta])
                        result[i] = (tmp[0], split)
                        delta += tmp_ - tmp[1] - 1
                    else:
                        split += int(times[delta + i])
                        result[i] = (tmp[0], split)
        # Sum of splits
        for j in range(len(result)):
            tmp = result[j]
            if j > 0:
                tmp_ = result[j - 1]
                result[j] = (tmp[0], tmp[1], tmp_[2] + tmp[1])
            else:
                result[j] = (tmp[0], tmp[1], tmp[1])
        check = result[0]
        if check[0] is not None and check[1] is not None:
            if len(result) == len(control_seq):
                passed = True
            else:
                passed = False
        else:
            passed = False
        for cp in judge_seq:
            if '|' in cp:
                judge_seq[temp_seq.index(cp)] = '<span class="approved">' + cp.replace('|', '') + '</span>'
            else:
                judge_seq[temp_seq.index(cp)] = '<span class="skipped">' + cp + '</span>'

        service_tup = (passed, total_time, points, judge_seq)
        return [service_tup] + result
    elif comp_type == 2:
        #a=[(111,11,11,11),('27', 650, 650),('27', 650, 650),('27', 650, 650),('27', 650, 650)]
        passed = True
        total_time = 0
        points = 0
        judge_seq=[]
        result=[('27', 1017, 1017), ('31', 1017, 1017), ('32', 1017, 1017)]
        temp_seq = seq
        judge_seq = temp_seq
        for j in seq:
            result.append(j)
            index = temp_seq.index(j)
            for o in range(0, index):
                temp_seq[o] = '.' + temp_seq[o]
            temp_seq[temp_seq.index(j)] = str(j)
            break
        # Cleanup
        judge_seq = []
        for p in temp_seq:
            temp_seq[temp_seq.index(p)] = p.replace('.', '')

        for cp in seq:
            judge_seq.append('<span class="approved">' + cp + '</span>')
        # Total time
        total_time = 0
        for sec in times:
            total_time += int(sec)
        # Points
        points = 0
        for res in result:
            if int(res[0]) > 30:
                points += int(res[0]) // 10


        service_tup = (passed, total_time, points, judge_seq)
        return [service_tup] + result


def generate_rand_seq(count):
    from random import randint
    seq = '27'
    for i in range(count):
        seq += '-' + str(randint(31, 110))
    seq += '-30'
    return seq


def generate_rand_punch(count):
    from random import randint
    punch = '0'
    for i in range(count-1):
        punch += '-' + str(randint(119, 659))
    return punch


def write_comp_id_to_file():
    from random import randint
    file = 'comp.txt'
    open(file, 'w').close()
    f = open(file, 'a')
    f.write(str(randint(0, 5)))
    f.close()
    write_update_to_file()


def read_comp_id_from_file():
    f = open('comp.txt', 'r')
    filedata = f.read()
    f.close()
    # print('Current ID: ' + filedata)
    return(filedata)


def write_update_to_file():
    from random import randint
    file = 'update.txt'
    open(file, 'w').close()
    f = open(file, 'a')
    f.write(str(randint(0, 255)))
    f.close()


def read_update_from_file():
    f = open('update.txt', 'r')
    filedata = f.read()
    f.close()
    # print('Update Code: ' + filedata)
    return (filedata)


def random_wrist_punch():
    from random import randint
    cp = randint(0, 255)
    if cp < 100:
        cp = cp + 900
    hh = randint(0, 24)
    if hh < 10:
        hh = '0' + str(hh)
    else:
        hh = str(hh)
    mm = randint(0, 60)
    if mm < 10:
        mm = '0' + str(mm)
    else:
        mm = str(mm)
    ss = randint(0, 60)
    if ss < 10:
        ss = '0' + str(ss)
    else:
        ss = str(ss)
    data = str(cp) + str(hh) + str(mm) + str(ss)
    return(int(data))


def convert_time(seconds):
    import time
    return(time.strftime('%H:%M:%S', time.gmtime(seconds)))
