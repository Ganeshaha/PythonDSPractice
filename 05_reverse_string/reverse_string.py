def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    phrase_list = [char for char in phrase]
    
    phrase_list.reverse()
    return "".join(phrase_list)

print(reverse_string('yeet'))