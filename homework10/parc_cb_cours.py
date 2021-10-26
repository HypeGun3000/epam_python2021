from xml.dom import minidom

import requests

url_cbank = "https://www.cbr.ru/scripts/XML_daily.asp?date_req="


def connect_to_centr_bank_RU(url_cbank):
    req_from_site = requests.get(url_cbank)
    src = req_from_site.text
    return src


def get_valute_course_in_rubles(char_code):
    """
    CHAR CODES:
    Фунт стерлингов : GBP
    Доллар США : USD
    Евро : EUR
    Китайский юань : CNY
    Украинских гривен : UAH
    Шведских крон : SEK
    Швейцарский франк : CHF
    Японских иен : JPY
    :param char_code:
    :return:
    """
    dom = minidom.parseString(connect_to_centr_bank_RU(url_cbank))

    elements = dom.getElementsByTagName("Valute")

    flag = True
    for node in elements:
        for child in node.childNodes:
            if child.nodeType == 1 and flag is True:
                if child.tagName == "CharCode":
                    char_code_of_valute = child.firstChild.data
                if child.tagName == "Value":
                    value_of_valute = float(child.firstChild.data.replace(",", "."))
        if char_code_of_valute == char_code:
            return value_of_valute
