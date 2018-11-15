from urllib.request import urlopen # For opening & reading URLs
from link_finder import LinkFinder
from general import *


class Spider:
    project_name = ""
    base_url = ""
    domain_name = ""
    page_url = ""
    queue_file = ""
    crawled_file = ""
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = queue_file + "/queued.txt"
        Spider.crawled_file = crawled_file + "/crawled.txt"
        self.boot()
        self.crawl_page("The first spider", Spider.base_url) 
    
    # Starts the program
    def boot(self):
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = set_to_file(Spider.crawled_file)

    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + "now crawling" + page_url)
            print("Queue: " + str(len(Spider.queue)) + "| Crawled: " + str(len(Spider.crawled))) # Length of queue/crawled files
            # Spider.add_links_to_queue(Spider.gather_link(page_url))
            # Spider.queue.remove(page_url)
            # Spider.crawled.add(page_url)
                                                            
