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
    def find(string: str):
        while '#' in string:
            try:
                backspace = string.index("#")
            except ValueError:
                return string
            if backspace == 0:
                string = string[1:]
            else:
                string = string[:backspace - 1] + string[backspace + 1:]
        return string

    if find(first) == find(second):
        return True
