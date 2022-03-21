from distutils.log import debug
from os import system
import re

data = """
park 800905-1049118
kim 700905-1059119
"""

result = []
for line in data.split("\n") :
    word_result = []
    for word in line.split(" ") :
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
            
        word_result.append(word)
        
    result.append(" ".join(word_result))
print("\n".join(result))

p = re.compile('[a-z]+')
m = p.match("python")

print(m.group())
print(m.start())
print(m.end())
print(m.span())

m = p.search("3 python")

print(m.group())
print(m.start())
print(m.end())
print(m.span())

result = p.findall("life is too short")
print(result)

result = p.finditer("life is too short")
print(result)

for r in result : print(r)

p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)
p = re.compile('[a-z]', re.I)
print(p.match('python'))
print(p.match('PYTHON'))

p = re.compile("^python\s\w+", re.MULTILINE)
data = """python one
python two
python three"""
print(p.findall(data))

chrref = re.compile(r'&[#](0[0-7]+|x[0-9a-fA-F]+);')
print(chrref)
chrref = re.compile(r"""&[#](
    0[0-7]+
    |[0-9]+
    |x[0-9a-fA-F]+
)
;
""", re.VERBOSE)
print(chrref)

p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)

print(re.search('^Life', 'Life is too short'))
print(re.search('^Life', 'My Life'))

print(re.search('short$', 'Life is too short'))
print(re.search('short$', 'Life is too short, you need python'))

p = re.compile(r'\bclass\b')
print(p.search('no class at all'))

p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))

print(p.search('the declassisfied algorithm'))

print(p.search('one subclass is'))

p = re.compile(r"\w+\s+\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m)

p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m.group(1))

p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name"))

p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())

p = re.compile('(blue|white|red)')
print(p.sub('color', 'blue socks and red shoes'))

p = re.compile('(blue|white|red)')
print(p.sub('color', 'blue socks and red shoes',count=1))

p = re.compile('(blue|white|red)')
print(p.sub('color', 'blue socks and red shoes',count=-2))

s = '<html><head><title>Title</title>'
print(len(s))
print(re.match('<.*>',s).span())
print(re.match('<.*>', s).group())