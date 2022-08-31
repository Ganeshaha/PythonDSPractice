from audioop import mul


def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    phrase_list = { char:phrase.count(char) for char in phrase}
    # object
    return phrase_list

print(multiple_letter_count('yeet yayYay'))
