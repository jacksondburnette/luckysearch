#lucky.py - Opens several Google search results
#Generic google search: https://www.google.com/search?q=SEARCH_TERM_HERE

import sys
import webbrowser

import bs4
import requests

print 'Googling...'
res = requests.get('http://google.com/search?q=' + ''.join(sys.argv[1:]))
try:
    res.raise_for_status()
except Exception as exc:
    print 'There was a problem: {}'.format(exc)

# TODO: Retreive top search result links
# TODO: Open a browser tab for each result
