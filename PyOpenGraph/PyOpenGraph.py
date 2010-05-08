#!/usr/bin/env python

#Copyright (c) 2010 Gerson Minichiello
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

import urllib
from HTMLParser import HTMLParser

class PyOpenGraph(object):
   
    types = {'activity':['activity', 'sport'],
        'business':['bar', 'company', 'cafe', 'hotel', 'restaurant'],
        'group':['cause' 'sports_league' 'sports_team'],
        'organization':['band', 'government', 'non_profit', 'school', 'university'],
        'person':['actor', 'athlete', 'author', 'director', 'musician', 'politician', 'public_figure'],
        'place':['city', 'country', 'landmark', 'state_province'],
        'product':['album', 'book', 'drink', 'food', 'game', 'isbn', 'movie', 'product', 'song', 'tv_show', 'upc'],
        'website':['article', 'blog', 'website']}
    
    def __init__(self, url):
        f = urllib.urlopen(url)
        contents = f.read()
        f.close()
        p = PyOpenGraphParser()
        p.feed(contents)
        p.close()
        self.metadata = p.properties
    
    def is_valid(self):
        required = set(['title', 'type', 'image', 'url'])
        if (set(self.metadata.keys()).intersection(required)) == required:
            return True
        else:
            return False
    
    def __str__(self):
        return self.metadata['title']
    
class PyOpenGraphParser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.properties = {}
    
    def handle_starttag(self, tag, attrs):
        if tag == 'meta':
            attrdict = dict(attrs)
            if attrdict.has_key('property') and attrdict['property'].startswith('og:') and attrdict.has_key('content'):
                self.properties[attrdict['property'].replace('og:', '')] = attrdict['content']

    def handle_endtag(self, tag):
        pass
    
    def error(self, msg):
        pass

if __name__ == '__main__':
    # Usage
    og = PyOpenGraph('http://www.rottentomatoes.com/m/10011268-oceans/')
    print og.metadata
    print og.metadata['title']