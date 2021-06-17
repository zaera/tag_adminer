from random import randint
import os

def write_comp_id_to_file():
    file = 'comp.txt'
    open(file, 'w').close()
    f = open(file, 'a')
    f.write(str(randint(0, 5)))
    f.close()


def read_comp_id_from_file():
    f = open('comp.txt', 'r')
    filedata = f.read()
    f.close()
    print('Current ID: ' + filedata)


def write_update_to_file():
    file = 'update.txt'
    open(file, 'w').close()
    f = open(file, 'a')
    f.write(str(randint(0, 255)))
    f.close()


def read_update_from_file():
    f = open('update.txt', 'r')
    filedata = f.read()
    f.close()
    print('Update Code: ' + filedata)


def random_wrist_punch():
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
