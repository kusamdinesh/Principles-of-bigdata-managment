import string
import re
import json

text = open("twiterdata.csv", "r")
# a = ""
b = []
c = []
for line in text.readlines():
    c = re.findall(r'\B#\w*[a-zA-Z]+\w*', line)
    if len(c) > 0:
        b.append(c)

print(b)
f = open('hashtags.txt', 'w')
f.write(json.dumps(b))