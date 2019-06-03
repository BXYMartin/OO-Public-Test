import re
from sys import argv

script, first = argv

lines = first.split('\n')
for line in lines:
    pattern = re.compile(r'\|[ ]*(\w+)[ ]*\|[ ]*(\w+)[ ]*\|')
    matcher = pattern.search(line)
    if matcher and matcher.group(2) == "UMLModel":
        print(matcher.group(1) + " ", end="")
