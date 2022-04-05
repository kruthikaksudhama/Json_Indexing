from bplustree import BplusTree
from bplustree import printTree

bpt = BplusTree(3)  #Number of keys in one node is passed as parameter
bpt.insert('aa', 5)
bpt.insert('ab', 3)
bpt.insert('bb', 10)
print(bpt.find('bb', 10))
#bpt.delete('aaa')
printTree(bpt)


