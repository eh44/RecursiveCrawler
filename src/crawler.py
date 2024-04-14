#!/usr/bin/python3  	  	  

#                         ,  	  	  
#                        (o)<  DuckieCorp Software License  	  	  
#                   .____//  	  	  
#                    \ <' )   Copyright (c) 2023 Erik Falor  	  	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	  	  
#         TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION  	  	  
#  	  	  
# You may reproduce and distribute copies of the Work in any medium,  	  	  
# with or without modifications, provided that You meet the following  	  	  
# conditions:  	  	  
#  	  	  
#   (a) You must give any other recipients of the Work a copy of this  	  	  
#       License; and  	  	  
#   (b) You must cause any modified files to carry prominent notices  	  	  
#       stating that You changed the files; and  	  	  
#   (c) You must retain, in the Source form of the files that You  	  	  
#       distribute, all copyright, patent, trademark, and attribution  	  	  
#       notices from the Source form of the Work; and  	  	  
#   (d) You do not misuse the trade names, trademarks, service marks,  	  	  
#       or product names of the Licensor, except as required for  	  	  
#       reasonable and customary use of the source files.  	  	  

# python -m pip install --user -r requirements.txt  	  	  
from bs4 import BeautifulSoup  	  	  
from urllib.parse import urlparse, urljoin, urldefrag  	  	  
import requests  	  	  
import sys  	  	  
import time
import traceback



def crawl(url, pastURL, maxDepth, currentDepth, URLVisitedBefore):
    """  	  	  
    Given an absolute URL, print each hyperlink found within the document.  	  	  
    This function will need more parameters.  	  	  

    Your task is to make this into a recursive function that follows hyperlinks  	  	  
    until one of two base cases are reached:  	  	  

    0) No new, unvisited links are found  	  	  
    1) The maximum depth of recursion is reached  	  	  
    """
    if maxDepth < currentDepth:
        return

    if not (urldefrag(url).url in URLVisitedBefore):
        for i in range(currentDepth):
            print("    ", end="")
        print(urldefrag(url).url)
    URLVisitedBefore.add(urldefrag(url).url)
    try:
        urlRequest = requests.get(url)
        ipAddress = BeautifulSoup(urlRequest.text, features="html.parser")
        #print(ipAddress)
        urlArray = [link.get('href') for link in ipAddress.find_all('a')]
        absoluteURL = []
        for i in range(len(urlArray)):
            absoluteURL.append(urljoin(pastURL, urlArray[i]))
            if urldefrag(absoluteURL[i]).url.split(':')[0].lower() == 'http' or \
                    urldefrag(absoluteURL[i]).url.split(':')[0].lower() == 'https':
                if not (urldefrag(absoluteURL[i]).url in URLVisitedBefore):
                    #print(absoluteURL[i])
                    crawl(absoluteURL[i], url, maxDepth, currentDepth+1,URLVisitedBefore)


    except(Exception):
        traceback.print_exc(None, None, True)
        return
    return  	  	  


# If the crawler.py module is loaded as the main module, allow our `crawl` function to be used as a command line tool  	  	  
if __name__ == "__main__":  	  	  

    ## If no arguments are given...  	  	  
    if len(sys.argv) < 2:  	  	  
        print("Usage Error: No arguments given. Please provide an absolute URL.", file=sys.stderr)
        exit(0)  	  	  
    else:  	  	  
        url = sys.argv[1]  	  	  
    if url.find('http://') != 0 and url.find('https://') != 0:
        print("Usage Error: URl must be absolute and start with http or https", file=sys.stderr)
        exit(0)
    maxDepth = 3
    if len(sys.argv) > 2:
        try:
            maxDepth = int(sys.argv[2])
        except TypeError:
             print("Usage Error: Max Depth must be an integer", file=sys.stderr)
             exit(0)
    plural = 's' if maxDepth != 1 else ''  	  	  
    print(f"Crawling from {url} to a maximum depth of {maxDepth} link{plural}")  	  	  
    startTime = time.time()
    URLVisitedBefore = set()
    try:

        crawl(url,url,maxDepth,0,URLVisitedBefore)
    except KeyboardInterrupt:
        print("exiting...")
    finally:
        timeTaken = time.time()-startTime
        print(f"Visited {len(URLVisitedBefore)} unique webpages in {timeTaken} seconds")
