import requests
from bs4 import BeautifulSoup as bs


BASE_URL = "https://isubtitles.org"


def results(query):
    r = requests.get(f"{BASE_URL}/search?kwd={query}").text
    soup = bs(r, "lxml")
    list_search = soup.find_all("div", class_="row")
    second_soup = bs(str(list_search), 'lxml')
    headings = second_soup.find_all("h3")
    third_soup = bs(str(headings), "lxml")
    search_links = third_soup.find_all("a")
    i = 0
    results = []
    for a in search_links:
        set = {
            "title": "",
            "keyword": "",
            "languages": {}
        }
        i += 1
        set['title'] = a.text
        key = a.get("href").split("/")
        set['keyword'] = key[1]
        index, language, link = get_lang(key[1])
        for i in range(len(index)):
            set['languages'][language[i-1]] = link[i-1]
        if set not in results:
            results.append(set)
    return results


def result(keyword):
    result = {
        "keyword": keyword,
        "languages": {}
    }
    index, language, link = get_lang(keyword)
    for i in range(len(index)):
        result['languages'][language[i-1]] = link[i-1]
    return result


def get_lang(keyword):
    url = f"{BASE_URL}/{keyword}"
    request = requests.get(url).text
    fourth_soup = bs(request, "lxml")
    filesoup = fourth_soup.find_all("table")
    fifth_soup = bs(str(filesoup), "lxml")
    table_soup = fifth_soup.find_all("a")
    language = []
    index = []
    link = []
    i = 0
    for b in table_soup:
        if b["href"].startswith("/download/"):
            i += 1
            h = b.get("href").split("/")
            buttoname = h[3]
            if buttoname not in language:
                index.append(i)
                language.append(buttoname)
                link.append(f"{BASE_URL}{b.get('href')}")
    return index, language, link
