def custom_range(*args):
    """
    Some of the functions have a bit cumbersome behavior when we deal with
    positional and keyword arguments.
    Write a function that accept any iterable of unique values and then
    it behaves as range function:
    import string
    assert = custom_range(string.ascii_lowercase, 'g')
     == ['a', 'b', 'c', 'd', 'e', 'f']
    assert = custom_range(string.ascii_lowercase, 'g', 'p')
    == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    assert = custom_range(string.ascii_lowercase, 'p', 'g', -2)
    == ['p', 'n', 'l', 'j', 'h']
    """
    sequence_of_numbers = []
    if len(args) == 2:
        for i in range(0, args[0].index(args[1])):
            sequence_of_numbers.append(i)
    elif len(args) == 3:
        for i in range(args[0].index(args[1]),
                       args[0].index(args[2])):
            sequence_of_numbers.append(i)
    elif len(args) == 4:
        for i in range(args[0].index(args[1]),
                       args[0].index(args[2]),
                       args[3]):
            sequence_of_numbers.append(i)
    return [args[0][i] for i in sequence_of_numbers]
