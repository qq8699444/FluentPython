## 3.2
DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan'),
    ]
country_code = {country:code for code, country in DIAL_CODES}
print(country_code)

code_country = {code:country.upper() for country,code in country_code.items() if code < 66}
print(code_country)

print("#####################################################")
# 3.3
import  sys
import re

WORD_RE = re.compile(r'\w+')

index = {}

with open(sys.argv[1],encoding='utf-8') as fp:
    for line_no,line in enumerate(fp,1):
        # print(line_no,line)
        for match in WORD_RE.finditer(line):
            word = match.group()
            cloumn_no = match.start() + 1
            location = (line_no,cloumn_no)
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences

for word in sorted(index,key=str.upper):
    print(word, index[word])
#################################################################
index.clear()
with open(sys.argv[1],encoding='utf-8') as fp:
    for line_no,line in enumerate(fp,1):
        # print(line_no,line)
        for match in WORD_RE.finditer(line):
            word = match.group()
            cloumn_no = match.start() + 1
            location = (line_no,cloumn_no)
            index.setdefault(word,[]).append(location)

for word in sorted(index,key=str.upper):
    print(word, index[word])

print("#####################################################")
# 3.4
import  collections
index2  = collections.defaultdict(list)
with open(sys.argv[1],encoding='utf-8') as fp:
    for line_no,line in enumerate(fp,1):
        # print(line_no,line)
        for match in WORD_RE.finditer(line):
            word = match.group()
            cloumn_no = match.start() + 1
            location = (line_no,cloumn_no)
            index2[word].append(location)

for word in sorted(index2,key=str.upper):
    print(word, index2[word])


class strKeyDict0(dict):
    def __missing__(self, key):
        print("strKeyDict0 missing")
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        print("strKeyDict0 get")
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, item):
        return key in self.keys() or str(key) in self.keys()


defaultdict1 = strKeyDict0()
defaultdict1["123"] = 123
defaultdict1["999"] = 999
print(defaultdict1[123])
print(defaultdict1.get(123))