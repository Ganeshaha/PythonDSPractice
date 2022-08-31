from re import T


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    dict1 = dict()
    dict2 = dict()
    list1 = list(f"{num1}")
    list2 = list(f"{num2}")

    for char in list1:
        dict1[char] = list1.count(char)
    for char in list2:
        dict2[char] = list2.count(char)
    if dict1 == dict2:
        return True
    else:
        return False
    
print(same_frequency(321142, 3212215))