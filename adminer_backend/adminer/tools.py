from random import randint


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
