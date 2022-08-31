def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase_list = phrase.split(" ")

    return f"{' '.join([char.capitalize() for char in phrase_list])}"

print(titleize('this is awesome'))
