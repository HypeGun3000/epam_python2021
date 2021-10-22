company_page_info = [[1, "5%"], [5, "65%"], [4, "7%"], [9, "21%"]]



print(sorted(company_page_info, key=lambda rubl: float((rubl[1])[:-1]), reverse=True)[:2])
