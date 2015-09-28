# Lief Swanson
# liefs@sfu.ca

from TwoThreeTree import TwoThreeTree

tree = TwoThreeTree()

functions = {
    "insert": tree.insert,
    "delete": tree.delete,
    "select": tree.select,
    "search": tree.search,
    "find": tree.search,
}

otherFunctions = {
    "exit": exit,
    "min": tree.min,
    "max": tree.max,
}

elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for elem in elements:
    tree.insert(elem)

print(tree.root.treeToList())

while True:
    x = input("> ")
    command = x.split()
    if len(command) == 2:
        function = command[0]
        arg = command[1]
        print(functions[function](int(arg)))
        print(tree)
    elif len(command) == 1:
        function = command[0]
        print(otherFunctions[function]())
        print(tree)
