def custom_range(*args):
    """
    Some of the functions have a bit cumbersome behavior when we deal with
    positional and keyword arguments.
    Write a function that accept any iterable of unique values and then
    it behaves as range function:
    import string
    assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
    assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
    """
    dic_asc = {}
    n = 0
    count = 0
    list_asc = []
    nlist_asc = []
    final_list = []
    for i in args[0]:
        if i not in dic_asc:
            dic_asc[i] = n
            n += 1
    for j in range(1, len(args)):
        list_asc.append(args[j])
    for o in list_asc:
        for k, v in dic_asc.items():
            if k == o:
                list_asc[count] = v
        count += 1

    if len(list_asc) == 1:
        for i in range(0, list_asc[0]):
            nlist_asc.append(i)
    elif len(list_asc) == 2:
        for i in range(list_asc[0], list_asc[1]):
            nlist_asc.append(i)
    elif len(list_asc) == 3:
        for i in range(list_asc[0], list_asc[1], list_asc[2]):
            nlist_asc.append(i)
    for i in nlist_asc:
        for k, v in dic_asc.items():
            if v == i:
                final_list.append(k)

    return final_list
