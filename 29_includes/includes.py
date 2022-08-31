def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    if start:
        if isinstance (collection, list):
            short_collection =collection[start:] 
            if sought in short_collection:
                return True
            else:
                return False
        if isinstance (collection, str):
            short_collection =collection[start:] 
            if sought in short_collection:
                return True
            else:
                return False
        
        if isinstance (collection, tuple):
            short_collection =collection[start:] 
            if sought in short_collection:
                return True
            else:
                return False
    else:
        if isinstance (collection, list):
            
            if collection.index(sought)>=0:
                return True
            else:
                return False
        if isinstance (collection, str):
            
            if sought in collection:
                return True
            else:
                return False
        if isinstance (collection, tuple):
            short_collection =collection[start:] 
            if sought in short_collection:
                return True
            else:
                return False
        if isinstance (collection, dict):
            
            if sought in collection.values:
                return True
            else:
                return False
        if isinstance (collection, set):
            
            if sought in collection:
                return True
            else:
                return False

print(includes({1, 2, 3}, 1))