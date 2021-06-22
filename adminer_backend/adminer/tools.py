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
