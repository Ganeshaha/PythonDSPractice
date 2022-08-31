def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    total = 0
    for p in parens:
        if p == '(':
            total += 1
        elif p == ')':
            total -= 1

        # fast fail: too many right parens
        if total < 0:
            return False

    return total == 0