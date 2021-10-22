company_page_info = [[1, "-0.5%"], [5, "-0.65%"], [4, "-1.7%"], [9, "-21%"]]

dictw = {
    "name": None,
    "valie": None
}
new_list = []
a = sorted(company_page_info, key=lambda rubl: float((rubl[1])[:-1]), reverse=False)[:2]
print(a)
for i in range(len(a)):
    for n, k in enumerate(dictw.keys()):
        dictw[k] = a[i][n]
    new_list.append(dictw.copy())
print(new_list)

