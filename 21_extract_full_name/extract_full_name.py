from unicodedata import name


def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    names_list =[]
    for char in people:
        names_list.append(f"{char['first']} {char['last']}")
    
    return names_list
names = [
     {'first': 'Ada', 'last': 'Lovelace'},
     {'first': 'Grace', 'last': 'Hopper'},
 ]

print(extract_full_names(names))