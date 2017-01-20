# Complete the method so that it does the following:

# Removes any duplicate query string parameters from the url
# Removes any query string parameters specified within the 2nd argument (optional array)
# Examples:

# stripUrlParams('www.codewars.com?a=1&b=2&a=2') // returns 'www.codewars.com?a=1&b=2'
# stripUrlParams('www.codewars.com?a=1&b=2&a=2', ['b']) // returns 'www.codewars.com?a=1'
# stripUrlParams('www.codewars.com', ['b']) // returns 'www.codewars.com'

import re
from urllib import urlencode
from urlparse import urlparse, urlunparse, parse_qs

def strip_url_params(url, params_to_strip = []):
    u = urlparse(url)
    print u
    query = parse_qs(u.query)
    print query

    #delete params to strip
    for x in params_to_strip:
        query.pop(x, None)
    
    #delete duplicate query string parameters
    dupl = []
    for x in query:
        if len(query[x]) > 1:
           dupl.append(x)      

    for x in dupl:
        del(query[x][-1:])

    u = u._replace(query=urlencode(query, True))
    return urlunparse(u)

if __name__ == '__main__':
    print strip_url_params('www.codewars.com?a=1&b=2&a=2')
    print strip_url_params('www.codewars.com?a=1&b=2&a=2', ['b'])
    #print strip_url_params('www.codewars.com', ['b'])
    