import requests
import xml.etree.ElementTree as ET
 

def get_feeds_url():
    is_adding_urls = True
    urls = []
    while is_adding_urls:
        url = input('Enter some RSS url:\n>')
        urls.append(url)
        check_if_adding = input("Any more urls ? (Y/N)")
        if(check_if_adding.lower() == 'n'): is_adding_urls = False
    return urls

def fetch_feed(url):
    res = requests.get(url)
    return res

def fetch_all_feeds(feeds_url):
    feeds = []
    for feed in feeds_url:
        feed = fetch_feed(feed).raw
        feeds.append(feed)
    return feeds
        
def parse_feed(feed):
    tree = ET.parse(feed)
    print(tree)
    # for child in root:
    #     print(child)

def main():
    feeds_urls = get_feeds_url()
    feeds = fetch_all_feeds(feeds_urls)
    parse_feed(feeds)
    
if __name__ == '__main__':
    main()