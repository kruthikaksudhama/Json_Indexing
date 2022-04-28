import bisect

# value[] stores [value, key1, ky2, key3, ...]
# child[] stores reference to child nodes
class BNode:
  def __init__(self, leaf):
      self.leaf = leaf
      self.value = [] # n
      self.child = [] # n+1
      

# n is the number of values that can be filled in one node
class BTree:
  def __init__(self, n):
    self.root = BNode(True)
    self.n = n
  

  # insert with recursion
  def insert_val(self, parent, root, val, rcp, bchild):
    # If root is not a leaf
    if(root.leaf == False):
      flag = 0
      for i in range(len(root.value)):
        if(val<root.value[i]):
          flag = 1
          break;
      if(flag == 1):
        root_ = self.insert_val(root, root.child[i], val, rcp, bchild)
      else:
        root_ = self.insert_val(root, root.child[len(root.value)], val, rcp, bchild)
      
      if(len(root_.value)>self.n):
        print("The node len is greater than", self.n, " so splitting ", root_.value)
        length = len(root_.value)
        middle = length // 2
        print("Moving ", root.value[middle], " to upper node")
        left_child = BNode(root_.leaf)
        right_child = BNode(root_.leaf)
        left_child.value = [a[0] for a in root_.value[:middle]]
        left_child.child = root_.child[:middle+1]
        right_child.value = [a[0] for a in root_.value[middle+1:]]
        right_child.child = root_.child[middle+1:]
        flag2 = 0
        for i in range(len(parent.value)):
          if(root_.value[middle]<parent.value[i]):
            flag2 = 1
            parent.value.insert[i, root_.value[middle]]
            parent.child = parent.child[:i] + [left_child, right_child] + parent.child[i+1:]
            break
        if(flag2 == 0):
          parent.value.append(root_.value[middle])
          parent.child = parent.child[:len(parent.child)-1]+[left_child, right_child]
    # If root is a leaf
    elif(root.leaf == True):
      flag3 = 0
      for i in range(len(root.value)):
        if(val == root.value[i][0]):
          flag3 = 1
          root.value[i].append(rcp)
          root.child[i].append(bchild)
      if(flag3 == 0):
        print("adding value to leaf node", [val, rcp])
        flag4 = 0
        for i in range(len(root.value)):
          if(val<root.value[i][0]):
            flag4 = 1
            root.value.insert(i, [val, rcp])
            root.child.insert(i, [bchild])
            break
        if(flag4 ==0):
          root.value.append([val, rcp])
          root.child.append([bchild])
      if(len(root.value)>self.n):
        print("The node len is greater than", self.n, " so splitting ", root.value)
        length = len(root.value)
        middle = length // 2
        print("Moving ", root.value[middle][0], " to upper node")
        left_child = BNode(root.leaf)
        right_child = BNode(root.leaf)
        left_child.value = root.value[:middle]
        left_child.child = root.child[:middle]
        right_child.value = root.value[middle:]
        right_child.child = root.child[middle:]
        flag2 = 0
        for i in range(len(parent.value)):
          if(root.value[middle][0]<parent.value[i]):
            flag2 = 1
            parent.value.insert(i, root.value[middle][0])
            parent.child = parent.child[:i] + [left_child, right_child] + parent.child[i+1:]
            break
        if(flag2 == 0):
          parent.value.append(root.value[middle][0])
          parent.child = parent.child[:len(parent.child)-1]+[left_child, right_child]
    return parent
      
  # value = search key
  # rcp = record pointer or document number
  # main insert function
  def insert_(self, value, rcp, bchild):
    print("hello2 ", value)
    root = self.root
    # corner case
    # If root is a leaf
    if(root.leaf == True):
      print("root is a leaf", root.value)
      # If there are no elements in the root
      if(len(root.value) == 0):
        print("root is empty", root.value)
        root.value.append([value, rcp])
        root.child.append([bchild])
        print("added ", [value, rcp], " to root ", root.value)
      else:
        print("root is not empty", root.value)
        flag3 = 0
        for i in range(len(root.value)):
          if(value == root.value[i][0]):
            flag3 = 1
            root.value[i].append(rcp)
            root.child[i].append(bchild)
            print("value already exists in the tree, so appending the key ", root.value)
        if(flag3 == 0):
          flag4 = 0
          for i in range(len(root.value)):
            if(value<root.value[i][0]):
              flag4 = 1
              root.value.insert(i, [value, rcp])
              root.child.insert(i, [bchild])
              break
          if(flag4 ==0):
            root.value.append([value, rcp])
            root.child.append([bchild])
          print([value, rcp], " is added to the root ", root.value)
        if(len(root.value)>self.n):
          print("the size of root ", len(root.value), " > ", self.n, "so splitting ", root.value)
          length = len(root.value)
          middle = length // 2
          print("the middle node ", root.value[middle], "is moved upward", root.value)
          temp = BNode(False)
          left_child = BNode(True)
          right_child = BNode(True)
          left_child.value = root.value[:middle]
          left_child.child = root.child[:middle]
          right_child.value = root.value[middle:]
          right_child.child = root.child[middle:]
          print("the left child is ", left_child.value, left_child.child, " the right child is ", right_child.value, right_child.child)
          temp.value.append(root.value[middle][0])
          temp.child = [left_child, right_child]
          self.root = temp
          print("the new root is ", self.root.value, self.root.child)
    else:
      # If root is not a leaf
      print("root is not a leaf")
      flag = 0
      for i in range(len(root.value)):
        if(value<root.value[i]):
          flag = 1
          break;
      if(flag == 1):
        print("calling the insert_val function")
        root_ = self.insert_val(root, root.child[i], value, rcp, bchild)
        print("return value of insert_val ", root_.value, "the root is ", self.root.value)
      else:
        print("calling the insert_val function")
        root_ = self.insert_val(root, root.child[len(root.value)], value, rcp, bchild)
        print("return value of insert_val ", root_.value, "the root is ", self.root.value)
      if(len(root_.value)>self.n):
        print("the node returned", len(root_.value), " is greater than ", self.n, "root is ", self.root.value)
        length = len(root_.value)
        middle = length // 2
        parent = BNode(False)
        left_child = BNode(root_.leaf)
        right_child = BNode(root_.leaf)
        left_child.value = root_.value[:middle]
        left_child.child = root_.child[:middle+1]
        right_child.value =root_.value[middle+1:]
        right_child.child = root_.child[middle+1:]
        print("the left child is ", left_child.value, left_child.child, " the right child is ", right_child.value, right_child.child)
        parent.value.append(root_.value[middle])
        parent.child = [left_child, right_child]
        self.root = parent
        print("the new root is ", self.root.value, self.root.child)

  def printTree(self, root):
    for i in range(len(root.value)):
      print(root.value[i], len(root.value))
    if(root.leaf == False):
      for i in range(len(root.child)):
        print("////")
        t = root.child[i]
        self.printTree(t)
    else:
      for i in range(len(root.child)):
        if(root.child[i][0] != None):
          print("child tree of ", root.value[i][0], "......................................")
          root.child[i][0].printTree(root.child[i][0].root)

  def search(self, root, value):
    if(root.leaf == False):
      flag = 0
      for i in range(len(root.value)):
        if(value<root.value[i]):
          flag = 1
          self.search(root.child[i], value)
          break
      if(flag == 0):
        self.search(root.child[len(root.value)], value)
    else:
      flag = 0
      for i in range(len(root.value)):
        if(value==root.value[i][0]):
          flag = 1
          print("The value ", value, "is in document number", root.value[i][1:])
          break
      if(flag ==0):
        print("The value ", value, "doen't exist in any document")

def main():
  B = BTree(2)
  B.insert_(12, 34)
  B.insert_(10, 23)
  B.insert_(1, 98)
  B.insert_(12, 3)

  B.printTree(B.root)

  B1 = BTree(3)
  B1.insert_(6, 100)
  B1.insert_(15, 101)
  B1.insert_(16, 102)
  B1.insert_(18, 103)
  B1.insert_(5, 104)
  B1.insert_(1, 105)
  B1.insert_(3, 106)
  B1.insert_(4, 107)
  B1.insert_(10, 108)
  B1.insert_(12, 109)
  B1.insert_(20, 110)
  B1.insert_(25, 111)
  B1.insert_(1, 120)
  B1.printTree(B1.root)
  B1.search(B1.root, 1)
  B1.search(B1.root, 2)

if __name__ == '__main__':
  main()


# # ///////////////////////////////////////////////////////////////////////////////////////
#       for i in range(len(root.value)):
#         if val < root.value[i]:
#           if(root.child[i] != None):
#             flag1 = 1
#             # insert the val in the child of parent
#             self.insert_val(root.child[i], val, rcp)
#           else:
#             # if there is no child to this node insert value and record pointer in this node
#             root.value.insert(i, [val, rcp])
#             # check the length of the node to match 'n', if greater than 'n', then divide
#             if len(root.value) > self.n:
#               length = len(root.value)
#               middle = length // 2
#               # if root is the actual root, then defined a new parent by dividing the root
#               if root == self.root:
#                 temp = BNode(False)
                
#                 # if root is a leaf
#                 if(root.leaf == True):
#                   left.value = root.value[:middle]
#                   right.value = root.value[middle:]
#                 # if root is not a leaf
#                 else:
#                   left.value = [a[0] for a in root.value[:middle]]
#                   right.value = [a[0] for a in root.value[middle+1:]]
#                   left.child = root.child[:middle+1]
#                   right.child = root.child[middle+1:]
#                 bisect.insort(temp.value, root.value[middle][0])
#                 temp.child = [left, right]
#                 self.root = temp
#               else:
#                 left = BNode(root.leaf)
#                 right = BNode(root.leaf)
#                 # if root is a leaf
#                 if(root.leaf == True):
#                   left.value = root.value[:middle]
#                   right.value = root.value[middle:]
#                 # if root is not a leaf
#                 else:
#                   left.value = [a[0] for a in root.value[:middle]]
#                   right.value = [a[0] for a in root.value[middle+1:]]
#                   left.child = root.child[:middle+1]
#                   right.child = root.child[middle+1:]
                

#       # if val is greater than all values in present node
#       if(flag1 == 0):

#     else:

