#!/Python27/python

import cgi
str = 'hello from cgi!'
print "Content-type: text/html\n\n"
print "%s" % str
