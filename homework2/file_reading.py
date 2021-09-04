from typing import List
import string


def get_longest_diverse_words(file_path: str) -> List[str]:
    """
    Find 10 longest words consisting from largest amount of unique symbols
    """
    lwords = []
    l10words = []
    finallist = []
    checkdic = {}
    with open(file_path) as fi:
        for i in fi:
            lwords.extend(i.split())
            for k in range(len(lwords)):
                for o in range(len(lwords[k])):
                    if lwords[k][o] not in checkdic:
                        checkdic[lwords[k][o]] = 1
                    else:
                        checkdic[lwords[k][o]] += 1
                flag = True
                for u in checkdic.values():
                    if u > 1:
                        flag = False
                        break
                if flag is True:
                    finallist.append(lwords[k])
            checkdic = {}
            lwords = []

        finallist = sorted(finallist, key=len, reverse=True)
        tencount = 10
        if len(finallist) < tencount:
            tencount = len(finallist)
        [l10words.append(finallist[j]) for j in range(tencount)]
        return l10words


def get_rarest_char(file_path: str) -> str:
    """
    Find rarest symbol for document
    """
    flist = []
    fulldic = {}
    raresym = []
    with open(file_path) as fi:
        for i in fi:
            flist.extend(i.split())
        for j in range(len(flist)):
            for k in range(len(flist[j])):
                if flist[j][k] not in fulldic:
                    fulldic[flist[j][k]] = 1
                else :
                    fulldic[flist[j][k]] += 1
        for o in fulldic.values():
            count = o
            break
        for k, v in fulldic.items():
            if v < count:
                count = v
        for k, v in fulldic.items():
            if v == count:
                raresym.append(k)
        return ', '.join(raresym)


def count_punctuation_chars(file_path: str) -> int:
    """
    Count every punctuation char
    """
    flist = []
    count = 0
    with open(file_path) as fi:
        for i in fi:
            flist.extend(i.split())
        for k in range(len(flist)):
            for j in range(len(flist[k])):
                if flist[k][j] in string.punctuation:
                    count += 1
    return count


def count_non_ascii_chars(file_path: str) -> int:
    """
    Count every non ascii char
    """
    flist = []
    with open(file_path) as fi:
        for i in fi:
            flist.extend(i.split())
    count = 0
    for k in range(len(flist)):
        for v in range(len(flist[k])):
            if flist[k][v] not in string.ascii_letters:
                count += 1
    return count


def get_most_common_non_ascii_char(file_path: str) -> str:
    """
    Find most common non ascii char for document
    :param file_path:
    :return:
    """
    flist = []
    nnascii = {}
    with open(file_path) as fi:
        for i in fi:
            flist.extend(i.split())
    for k in range(len(flist)):
        for v in range(len(flist[k])):
            if flist[k][v] not in string.ascii_letters:
                if flist[k][v] not in nnascii:
                    nnascii[flist[k][v]] = 1
                else:
                    nnascii[flist[k][v]] += 1
    count = 0
    for k, v in nnascii.items():
        if v >= count:
            count = v
    for k, v in nnascii.items():
        if v == count:
            return k
print(get_most_common_non_ascii_char("data.txt"))