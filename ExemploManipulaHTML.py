#!/usr/bin/env python
from html.parser import HTMLParser
from urllib import request

class MeuParser(HTMLParser):
   def handle_starttag(self, tag, attrs):
      print ("abre %s" % tag)

   def handle_endtag(self, tag):
      print ("fecha %s" % tag)

p = MeuParser()
doc = request.urlopen('http://www.facebook.com').read()
p.feed(doc)