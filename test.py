from bplustree import BplusTree
from bplustree import printTree

bpt = BplusTree(4)  #Number of keys in one node is passed as parameter
bpt.insert('aa', 3)
bpt.insert('aa', 4)
bpt.insert('ab', 4)
bpt.insert('ac', 4)
bpt.insert('ad', 4)
bpt.insert('ae', 4)
bpt.insert('af', 4)
print(dir(bpt))
#print(bpt.root.values)
printTree(bpt)
print(bpt.search('ff').values)
