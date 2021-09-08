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
    dictionary_of_ascii_sym = {}
    number_of_symbol = 0
    count = 0
    list_of_symbols_from_function = []
    sequence_of_numbers = []
    sequence_of_chars = []
    for i in args[0]:
        if i not in dictionary_of_ascii_sym:
            dictionary_of_ascii_sym[i] = number_of_symbol
            number_of_symbol += 1
    for j in range(1, len(args)):
        list_of_symbols_from_function.append(args[j])
    for o in list_of_symbols_from_function:
        for k, v in dictionary_of_ascii_sym.items():
            if k == o:
                list_of_symbols_from_function[count] = v
        count += 1

    if len(list_of_symbols_from_function) == 1:
        for i in range(0, list_of_symbols_from_function[0]):
            sequence_of_numbers.append(i)
    elif len(list_of_symbols_from_function) == 2:
        for i in range(list_of_symbols_from_function[0],
                       list_of_symbols_from_function[1]):
            sequence_of_numbers.append(i)
    elif len(list_of_symbols_from_function) == 3:
        for i in range(list_of_symbols_from_function[0],
                       list_of_symbols_from_function[1],
                       list_of_symbols_from_function[2]):
            sequence_of_numbers.append(i)
    for i in sequence_of_numbers:
        for k, v in dictionary_of_ascii_sym.items():
            if v == i:
                sequence_of_chars.append(k)

    return sequence_of_chars
