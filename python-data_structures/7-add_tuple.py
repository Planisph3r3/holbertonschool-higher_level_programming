#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    counter = 0
    if len(tuple_b) < 2 or len(tuple_a) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))
        tuple_a += (0,) * (2 - len(tuple_a))

    elif len(tuple_b) > 2 or len(tuple_a) > 2:
        if counter != 2:
            for i in range(len(tuple_a)):
                if i == 2:
                    return tuple_c
                sum_tuple = tuple_a[i] + tuple_b[i]
                tuple_c += (sum_tuple,)
                counter += 1
    for i in range(2):
        sum_tuple = tuple_a[i] + tuple_b[i]
        tuple_c += (sum_tuple,)
    return tuple_c
