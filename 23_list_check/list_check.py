def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    all_is_list = True
    for char in lst:
        if not isinstance(char, list):
            all_is_list = False
    return all_is_list

print(list_check([[1], "nope"]))

