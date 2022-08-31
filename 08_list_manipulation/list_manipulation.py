def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    command_lowered = command.lower()
    location_lowered = location.lower()
    if  command_lowered == 'remove':
        if location_lowered == 'beginning':
            return lst.pop(0)
        elif location_lowered =='end':
            return lst.pop()

    elif command_lowered == 'add':
        if location_lowered == 'beginning':
            lst.insert(0, value)
            return lst
        elif location_lowered =='end':
            lst.insert(len(lst)-1,value)
            return lst

    else: 
        return "Invalid command"    


lst = [1, 2, 3]

print(list_manipulation(lst, 'add', 'beginning', 20))