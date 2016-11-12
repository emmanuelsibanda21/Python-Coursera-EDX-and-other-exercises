import urllib
fhand = urllib.urlopen('http://data.pr4e.org/intro-short.txt')
for line in fhand:
    print line.strip()
http_message = fhand.info()
full = http_message.type
main = http_message.maintype
print main
print full
print http_message
