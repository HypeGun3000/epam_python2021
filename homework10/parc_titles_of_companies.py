import datetime
from bs4 import BeautifulSoup
import requests
import lxml
from homework10.parc_cb_cours import get_valute_course_in_rubles

url_site = "https://markets.businessinsider.com/index/components/s&p_500?p="

headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }

list_of_year_results = {}
list_of_latest_price = {}
list_of_information_from_all_title_pages = []
list_of_all_links = []
company_page_info = []


def get_title_information_from_all_pages(url_site: str, headers: dict):
    global list_of_information_from_all_title_pages
    count_page = 1
    while True:
        req_from_site = requests.get(url_site + str(count_page), headers=headers)
        src = req_from_site.text
        soup = BeautifulSoup(src, "lxml")
        try:
            all_companies_info_title = soup.find(class_="table__tbody").find_all("tr")
        except AttributeError:
            return list_of_information_from_all_title_pages
        for i in all_companies_info_title:
            list_of_information_from_one_page = []
            information_by_lines = i.text.strip().splitlines()
            for line in information_by_lines:
                if line != '' and "\t" not in line:
                    list_of_information_from_one_page.append(line)
            list_of_information_from_all_title_pages.append(list_of_information_from_one_page)
        count_page += 1


def get_price_in_rubles():
    for i in range(len(company_page_info)):
        company_page_info[i].append(round(float(list_of_information_from_all_title_pages[i][1].replace(',', '')) * get_valute_course_in_rubles("USD"), 2))
    return company_page_info


def get_year_groth():
    for i in range(len(company_page_info)):
        company_page_info[i].append(list_of_information_from_all_title_pages[i][-1])
    return company_page_info


def get_links_for_all_companies(headers: dict):
    global list_of_all_links
    url_site_official = "https://markets.businessinsider.com/"
    count_page = 1
    while True:
        request = requests.get(url_site + str(count_page), headers=headers)
        src = request.text
        soup = BeautifulSoup(src, 'lxml')
        try:
            links = soup.find(class_="table__tbody").find_all("a")
        except AttributeError:
            return list_of_all_links
        for item in links:
            list_of_all_links.append((url_site_official + item.get("href")))
        count_page += 1


def get_information_from_every_company_page(headers: dict):
    timer = 1
    global company_page_info
    list_of_one_company_code_name = []
    for link in list_of_all_links:
        request = requests.get(link, headers=headers)
        src = request.text
        soup = BeautifulSoup(src, 'lxml')
        company_code = soup.find(class_="price-section__category")
        company_name = soup.find(class_="price-section__label")
        company_p_e = soup.find_all(class_="snapshot__data-item")
        for i in company_p_e:
            if "P/E Ratio" in i.text:
                ratio_company = i.text.strip().split()
        company_potential_profit_low = soup.find_all(class_="snapshot__data-item snapshot__data-item--small")
        company_potential_profit_high = soup.find_all(class_="snapshot__data-item snapshot__data-item--small snapshot__data-item--right")
        for i in company_potential_profit_low:
            if "Week" in i.text:
                low_week = float(i.text.strip().split()[0].replace(",", ""))

        for i in company_potential_profit_high:
            if "Week" in i.text:
                high_week = float(i.text.strip().split()[0].replace(",", ""))

        list_of_one_company_code_name.append(company_name.text.strip())
        list_of_one_company_code_name.append(company_code.text.strip().split(', ')[-1])
        list_of_one_company_code_name.append(ratio_company[0])
        list_of_one_company_code_name.append(round((high_week - low_week), 2))
        company_page_info.append(list_of_one_company_code_name)
        list_of_one_company_code_name = []
        print(timer)
        timer += 1
    return company_page_info


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    get_links_for_all_companies(headers)
    get_information_from_every_company_page(headers)
    get_title_information_from_all_pages(url_site, headers)
    get_price_in_rubles()
    print(get_year_groth())
    print(sorted(company_page_info, key=lambda rubl: rubl[4], reverse=True)[:10])
    print(sorted(company_page_info, key=lambda rubl: rubl[2], reverse=False)[:10])
    print(sorted(company_page_info, key=lambda rubl: float((rubl[5])[:-1]), reverse=True)[:10])
    print(sorted(company_page_info, key=lambda rubl: rubl[3], reverse=True)[:10])
    print(datetime.datetime.now() - start_time)


