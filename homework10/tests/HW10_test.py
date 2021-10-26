import urllib

from homework10.parc_cb_cours import (connect_to_centr_bank_RU,
                                      get_valute_course_in_rubles)
from homework10.parc_titles_of_companies import (
    add_information_in_dicts, add_json_files, convert_dollars_in_rub,
    get_info_from_company, get_information_from_every_company_page,
    get_links_for_all_companies, get_price_in_rubles,
    get_title_information_from_all_pages, get_year_groth,
    multiprocessing_convert)

import pytest
from urllib.request import urlopen
import requests

url_cbank = "https://www.cbr.ru/scripts/XML_daily.asp?date_req="


class TestCBconvert:

    url_cbank = "https://www.cbr.ru/scripts/XML_daily.asp?date_req="

    def test_connecting_cb(self):
        assert connect_to_centr_bank_RU("https://www.cbr.ru/scripts/XML_daily.asp?date_req=")

    def test_not_exist_url(self):
        with pytest.raises(requests.exceptions.ConnectionError):
            assert connect_to_centr_bank_RU("https://asfas3332221fas.com") is True

