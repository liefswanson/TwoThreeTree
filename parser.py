# Lief Swanson
# liefs@sfu.ca

from sys import argv
from TwoThreeTree import TwoThreeTree

tree = TwoThreeTree()

functions = {
    "insert": tree.insert,
    "delete": tree.delete,
    "find": tree.insert,
    "selection": tree.select,
    "select": tree.select,
}

path = argv[0]

f = open(path, 'r')

lines = f.split('\n')
nums  = [int(num) for num in lines.pop(0).split(',')]

for num in nums:
    tree.insert(num)

for line in lines:
    args = line.split()
    function = args[0]
    value = args[1]

    functions[function](value)
