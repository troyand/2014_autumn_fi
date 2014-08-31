import re
import urllib2


distedu_index = urllib2.urlopen('http://distedu.ukma.kiev.ua/')

print '\n'.join(re.findall(
    r'http:\/\/distedu.ukma.kiev.ua/file.php/1/2014-2015o/.*\.doc',
    distedu_index.read()))
