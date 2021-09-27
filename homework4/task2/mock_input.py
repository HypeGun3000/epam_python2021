import urllib
from urllib.request import urlopen


def get_body(url):
    try:
        response = urlopen(url)
    except urllib.error.URLError:
        raise urllib.error.URLError("url does not exist")
    if response.code == 200:
        data = response.read()
        html = data.decode("UTF-8")
        return html


def count_dots_on_i(url: str) -> int:
    html = get_body(url)
    letter_count = html.count("i")
    return letter_count
