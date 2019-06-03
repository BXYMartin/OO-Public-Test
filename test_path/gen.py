import os, re
from sys import argv
import random

choice = [
        "CLASS_COUNT",
        "CLASS_OPERATION_COUNT",
        "CLASS_ATTR_COUNT",
        "CLASS_ASSO_COUNT",
        "CLASS_ASSO_CLASS_LIST",
        "CLASS_OPERATION_VISIBILITY",
        "CLASS_ATTR_VISIBILITY",
        "CLASS_TOP_BASE",
        "CLASS_IMPLEMENT_INTERFACE_LIST",
        "CLASS_INFO_HIDDEN"
        ]
opmode = [
        "NON_RETURN",
        "RETURN",
        "NON_PARAM",
        "PARAM",
        "ALL"
        ]

atmode = [
        "SELF_ONLY",
        "ALL"
        ]

def find():
    return re.findall(r'"name":"(\w+)"', first)

script, first = argv

get=find()

while 'null' in get:
    get.remove('null')

gen=""

n = 800

for i in range(n):
    ins = random.choice(choice)
    gen = gen + ins
    if ins == "CLASS_COUNT":
        pass
    elif ins == "CLASS_ASSO_COUNT" or ins == "CLASS_TOP_BASE" or ins == "CLASS_INFO_HIDDEN" or ins == "CLASS_IMPLEMENT_INTERFACE_LIST" or ins == "CLASS_ASSO_CLASS_LIST":
        gen = gen + " " + random.choice(get)
    elif ins == "CLASS_OPERATION_COUNT":
        gen = gen + " " + random.choice(get) + " " + random.choice(opmode)
    elif ins == "CLASS_ATTR_COUNT":
        gen = gen + " " + random.choice(get) + " " + random.choice(atmode)
    elif ins == "CLASS_OPERATION_VISIBILITY" or ins == "CLASS_ATTR_VISIBILITY":
        gen = gen + " " + random.choice(get) + " " + random.choice(get)
    if i != n - 1:
        gen = gen + "\n"

print(gen)
