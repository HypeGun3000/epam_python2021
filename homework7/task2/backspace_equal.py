def backspace_compare(first: str, second: str):
    """
    Given two strings. Return if they are equal
    when both are typed into
    empty text editors. # means a backspace character.
    Note that after backspacing an empty text,
    the text will continue empty.
    Examples:
        Input: s = "ab#c", t = "ad#c"
        Output: True
        # Both s and t become "ac".
        Input: s = "a##c", t = "#a#c"
        Output: True
        Explanation: Both s and t become "c".
        Input: a = "a#c", t = "b"
        Output: False
        Explanation: s becomes "c" while t becomes "b".
    """
    while '#' in first:
        if first.startswith('#'):
            first = first[1:]
        if first[-1] == '#':
            first = first[:-2]
        if '#' in first:
            ind_char = first.index("#")
            first = first[:ind_char-1] + first[ind_char+1:]
    while '#' in second:
        if second.startswith('#'):
            second = second[1:]
        if second[-1] == '#':
            second = second[:-2]
        if '#' in second:
            ind_char = second.index("#")
            second = second[:ind_char-1] + second[ind_char+1:]
    if first == second:
        return True
    else:
        return False
