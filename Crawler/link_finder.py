# This file parses through html script of any website to scrape links
from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # Locates links in website's html code
    def handle_starttag(tag, attrs):
        if tag == "a":
            for (attribute, value) in attrs:
                if attribute == "href":
                    url = parse.urljoin(self.base_url, value) 
                    self.links.add(url)
    
    # Returns parsed set of links from the html code
    def page_links(self):
        return self.links
    
    # Passes an error message
    def error_message(self, message):
        pass

    