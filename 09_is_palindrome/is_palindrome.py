from operator import truediv


def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase_lowered = phrase.lower()
    phrase_list = [char for char in phrase_lowered]
    phrase_list_reversed = phrase_list.copy()
    phrase_list_reversed.reverse()

    if phrase_list == phrase_list_reversed:
        return True
    else:
        return False

print(is_palindrome('tacocat'))
print(is_palindrome('Noon'))