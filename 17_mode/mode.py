def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    highest_count = 0
    highest_char = 0

    for char in nums:
        if nums.count(char)>highest_count:
            highest_count = nums.count(char)
            highest_char = char
    return highest_char

print(mode([2, 2, 3, 3, 2]))

