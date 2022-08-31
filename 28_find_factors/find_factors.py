from unittest import skip


def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    factor_list =[]
    for x in range(num+1):
        if x == 0:
            continue
        if num%x ==0:
            factor_list.append(x)

    return factor_list

print(find_factors(111))

