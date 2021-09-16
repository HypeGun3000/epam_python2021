import urllib.request
from mock import Mock
import unittest.mock
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
    count_of_i = 0
    get_html_code = urllib.request.urlopen(url)
    html_text = get_html_code.read().decode("utf-8")
    soup = BeautifulSoup(html_text, "html.parser")
    raw_text_form_site = soup.get_text()
    raw_text_form_siteMock = Mock(soup.get_text())
    for i in raw_text_form_site:
        if i == "i":
            count_of_i += 1
    return count_of_i


#print(count_dots_on_i("https://example.com/"))
