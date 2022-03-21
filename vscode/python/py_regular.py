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