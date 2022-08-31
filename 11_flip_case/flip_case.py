def flipper(char):
    if char >= 'A' and char <= 'Z':
        return char.lower()
    elif char >= 'a' and char <= 'z':
        return char.upper()


def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    phrase_swapped = [flipper(char) if to_swap == flipper(char) or to_swap == char else char for char in phrase]
    return ''.join(phrase_swapped)

print(flip_case('Aaaahhh', 'h'))