<<<<<<< HEAD
from urllib.request import urlopen


def get_body(url):
    try:
        response = urlopen(url)
        if response.code == 200:
            data = response.read()
            html = data.decode("UTF-8")
            return html
    except Exception:
        raise ValueError("url doesn't exist")


def count_dots_on_i(url: str) -> int:
    html = get_body(url)
    letter_count = html.count("i")
    return letter_count


=======
import urllib.request
from bs4 import BeautifulSoup


def count_dots_on_i(url: str) -> int:
    """
    Write a function that accepts an URL as input
    and count how many letters `i` are present in the HTML by this URL.
    Write a test that check that your function works.
    Test should use Mock instead of real network interactions.
    You can use urlopen* or any other network libraries.
    In case of any network error raise ValueError("Unreachable {url}).
    Definition of done:
     - function is created
     - function is properly formatted
     - function has positive and negative tests
     - test could be run without internet connection
    You will learn:
     - how to test using mocks
     - how to write complex mocks
     - how to raise an exception form mocks
     - do a simple network requests
    >>> count_dots_on_i("https://example.com/")
    22
    * https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
    """
    return get_text_from_site(url).count("i")


def get_text_from_site(url):
    try:
        get_html_code = urllib.request.urlopen(url)
        if get_html_code.code == 200:
            html_text = get_html_code.read().decode("utf-8")
            soup = BeautifulSoup(html_text, "html.parser")
            raw_text_form_site = soup.get_text()
            return raw_text_form_site
    except urllib.error.URLError:
        print("Not true URL")



>>>>>>> 5a56de98d950f1ab94a87e14636499634a9da67d
print(count_dots_on_i("https://example.com/"))
