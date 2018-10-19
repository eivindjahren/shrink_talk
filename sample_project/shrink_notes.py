import pandas as pd
from demoapp.calculate import Calculate
import numpy as np
np.seterr(all='raise')

def shrink_int(a):
    if a == 0:
        return [0]
    return [0] + ([-a] if a < 0 else []) + dichotomy(a,a/2)

def dichotomy(a,b):
    if abs(b) <= 0:
        return []
    return [a-b] + dichotomy(a,int(float(b)/2))


def this_should_fail(a, b):
    return a + a + b == a + b

def shrink_test():
    a = 100
    b = -34

    shrink_limit = 10
    for _ in range(shrink_limit):
        for shrink_a in shrink_int(a):
            if not this_should_fail(shrink_a, b):
                a = shrink_a
                break
        for shrink_b in shrink_int(b):
            if not this_should_fail(a, shrink_b):
                b = shrink_b
                break
    print(a,b)


def shrink_list(a):
    yield []
    for i, _ in enumerate(a):
        b = a[:]
        del b[i]
        yield b
    for i, c in enumerate(a):
        for d in shrink_int(c):
            b = a[:]
            b[i] = d
            yield b

def this_should_fail2(a):
    b = a[:]
    b.sort()
    return b == a

def shrink_test2():
    a = [3,2,1]

    shrink_limit = 10
    for _ in range(shrink_limit):
        for shrink_a in shrink_list(a):
            if not this_should_fail2(shrink_a):
                a = shrink_a
                break
    print(a)

def shrink_dataframe(df):
    for column in df.columns:
        yield df.drop(column, axis=1)
    for row in range(len(df.index)):
        yield df.drop(df.index[row])
    for column in df.columns:
        for row in range(len(df.index)):
            el = df[column].iloc[row]
            for shrink_element in shrink_int(el):
                df2 = df.copy()
                df2[column].iloc[row] = shrink_element
                yield df2

def this_should_fail3(df):
    if (df == 0).any().any():
        return True
    calc = Calculate(df)
    try:
        calc.calculate()
        return True
    except:
        return False

def shrink_test3():
    a = pd.DataFrame.from_csv('test.csv')

    shrink_limit = 1100
    for _ in range(shrink_limit):
        for shrink_a in shrink_dataframe(a):
            if not this_should_fail3(shrink_a):
                a = shrink_a.copy()
                break
    print(a)
