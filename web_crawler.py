# -----------------------------------------------------------------------------
# Name:        crawler.py
# Purpose:     CS21A Assignment # 8 - implement a simple web crawler
#
# Author:   Shan
# -----------------------------------------------------------------------------
"""
implement a simple web crawler

Usage: crawler.py seed_url
seed: absolute url - the crawler will use it as the initial web address
"""

import urllib.request
import urllib.parse
import urllib.error
import urllib.robotparser
import re
import sys
import string

MAX_URLS = 10

# DO NOT CHANGE ok_to_crawl!!!
def ok_to_crawl(absolute_url):
    """
    check if it is OK to crawl the specified absolute url

    We are implementing polite crawling by checking the robots.txt file
    for all urls except the ones using the file scheme (these are urls
    on the local host and they are all OK to crawl.)
    We also use this function to skip over mailto: links and javascript: links.
    Parameter:
    absolute_url (string):  this is an absolute url that we would like to crawl
    Returns:
    boolean:  True if the scheme is file (it is a local webpage)
              True if we successfully read the corresponding robots.txt
                   file and determined that user-agent * is allowed to crawl
              False if it is a mailto: link or a javascript: link
                   if user-agent * is not allowed to crawl it or
                   if it is NOT an absolute url.
    """
    if absolute_url.lower().startswith('mailto:'):
        return False
    if absolute_url.lower().startswith('javascript:'):
        return False
    link_obj = urllib.parse.urlparse(absolute_url)
    if link_obj.scheme.lower().startswith('file'):
        return True
    # check if the url given as input is an absolute url
    if not link_obj.scheme or not link_obj.hostname:
        print('Not a valid absolute url: ', absolute_url)
        return False
    # construct the robots.txt url from the scheme and host name
    else:
        robot_url = link_obj.scheme + '://' + link_obj.hostname + '/robots.txt'
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(robot_url)
        try:
            rp.read()
        except:
            print("Error accessing robot file: ", robot_url)
            return False
        else:
            return rp.can_fetch("*", absolute_url)


# DO NOT CHANGE crawl!!!
def crawl(seed_url):
    """
    start with the seed_url and crawl up to 10 urls

    Parameter:
    seed_url (string) - this is the first url we'll visit.
    Returns:
    set of strings - set of all the urls we have visited.
    """
    urls_tocrawl = {seed_url}  # initialize our set of urls to crawl
    urls_visited = set()  # initialize our set of urls visited
    while urls_tocrawl and len(urls_visited) < MAX_URLS:
        current_url = urls_tocrawl.pop()  # just get any url from the set
        if current_url not in urls_visited:  # check if we have crawled it
            page = get_page(current_url)
            if page:
                more_urls = extract_links(current_url, page)  # get the links
                urls_tocrawl = urls_tocrawl | more_urls  # add them
                urls_visited.add(current_url)
    return urls_visited


# ------------Do not change anything above this line----------------------------

def get_page(url):
    # TO DO:
    # get_page takes an absolute url as input parameter
    # and returns a string that contains the web page pointed to by that url.
    # Assume the web page uses utf-8 encoding.
    # If there is an error opening the url or decoding the content,
    # print a message identifying the url and the error and
    # return an empty string.
    # Use the with construct to open the url.
    """
    get the page content from giving absolute url

    :param url: absolute url
    :return: page content
    """

    try:
        with urllib.request.urlopen(url) as url_file:
            byte_page = url_file.read()
            page = byte_page.decode('UTF-8')
    except urllib.error.URLError as url_err:
        print('Error open url', url, url_err)
        page = ''
    except UnicodeDecodeError as decode_err:
        print('Error open url',url,decode_err)
        page = ''

    return page


def extract_links(base_url, page):
    """
    extract the links contained in the page at the base_url
    Parameters:
    base_url (string): the url we are currently crawling - web address
    page(string):  the content of that url - html
    Returns:
    A set of absolute urls (set of strings) - These are all the urls extracted
        from the current url and converted to absolute urls.

    """
    # TO DO:
    # write the code for extract_links.
    # 1. Initialize an empty set for the urls
    # 2. use a re pattern to extract the urls from the html file
    # 3. make sure you extract ALL the URLs on that page
    # 4. convert each link to an absolute url (hint: urllib.parse.urljoin())
    # 5. call the function ok_to_crawl to check if you are allowed
    #    to crawl that absolute url
    # 6. If that url is ok_to_crawl, add it to the set of urls
    #    found on that page.
    # 7. Return the set of urls
    url_set = set()
    pattern = r'href\s*=\s*([\'"]?[^\'">]+\.html)'
    all_matches = re.finditer(pattern, page)
    for url_match in all_matches:
        url_unit = url_match.group(1)
        each_url = urllib.parse.urljoin(base_url, url_unit.strip(string.punctuation))
        if ok_to_crawl(each_url):
           url_set.add(each_url)

    return url_set

def main():

# TO DO:
# 1.get the seed_url from the command line arguments
# 2.crawl_path = crawl(seed_url)
# 3.print out all the urls in crawl_path to a file called crawled.txt
#   in the working directory.  Make sure you print one url per line.


    if len(sys.argv) != 2:
        print("incorrect length of argument")
    else:
        seed_url = sys.argv[1]
        crawl_path=crawl(seed_url)

        with open('crawled.txt','w',encoding='utf-8') as final_file:
            for path in crawl_path:
                final_file.write(path+'\n')


if __name__ == '__main__':
    main()