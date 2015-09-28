# Lief Swanson
# liefs@sfu.ca

import TwoThreeTree

a = TwoThreeTree.TwoThreeTree()

l = [1, 2, 5, 7, 9, 5, 6, 8, 3, 2, 5, 4, 10, 9, 7, 5, -1, -4, 2, -2]
# l = [0,-1,-2,-3,-4,-5,-6,-7]
for i in range(len(l)):
    print("inserting... " + str(l[i]))
    input()
    a.insert(l[i])
    print(a)
