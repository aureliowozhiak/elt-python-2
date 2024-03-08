import requests
import bs4

class Extract:
    def __init__(self, url):
        self.url = url
        self.soup = self.html_to_soup()

    def get_html(self):
        response = requests.get(self.url)
        return response.text

    def html_to_soup(self):
        html = self.get_html()
        soup = bs4.BeautifulSoup(html, 'html.parser')
        return soup

    def get_tags(self, tag):
        tags = self.soup.find_all(tag)
        return tags