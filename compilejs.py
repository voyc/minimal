#!/usr/bin/python2.4

import httplib, urllib, sys

# Define the parameters for the POST request and encode them in
# a URL-safe format.

params = urllib.urlencode([
	('code_url', 'http://minimal.hagstrand.com/icon/icon.js'),
	('code_url', 'http://minimal.hagstrand.com/icon/lib/menu.js'),
	('code_url', 'http://minimal.hagstrand.com/icon/lib/gear.js'),
	('code_url', 'http://minimal.hagstrand.com/jslib/utils.js'),
	('code_url', 'http://minimal.hagstrand.com/jslib/dragger.js'),
	('code_url', 'http://minimal.hagstrand.com/minimal.js'),
	('compilation_level', 'ADVANCED_OPTIMIZATIONS'),
	('language', 'ECMASCRIPT5'),
	('output_format', 'text'),
	('output_info', 'compiled_code'),
	#('formatting', 'pretty_print'),
])

# Always use the following value for the Content-type header.
headers = { "Content-type": "application/x-www-form-urlencoded" }
conn = httplib.HTTPConnection('closure-compiler.appspot.com')
conn.request('POST', '/compile', params, headers)
response = conn.getresponse()
data = response.read()
print data
conn.close()
