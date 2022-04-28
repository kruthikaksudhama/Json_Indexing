import json
from BplusTree import BTree, BNode

def insertToBTree(tree, doc_num, key, value):

    if(type(value) == dict):
        for k, v in value.items():
            B1 = BTree(4)
            print("hi1")
            print("value is dict,  k=",k, "type = ", type(k), "v=", v, "type = ", type(v))
            B1 = insertToBTree(B1, doc_num, k, v)
            print("Value ", v, "added to ")
            B1.printTree(B1.root)
        tree.insert_(key, doc_num, B1)

    elif(type(value) == list):
        print("hi2")
        B1 = BTree(4)
        for i in range(len(value)):
            print("list  --  ", value[i])
            B1.insert_(value[i], doc_num, None)
        tree.insert_(key, doc_num, B1)
        return tree

    elif(type(value) == str):
        print("hi3")
        B1 = BTree(4)
        B1.insert_(value, doc_num, None)
        B1.printTree(B1.root)
        tree.insert_(key, doc_num, B1)
        return tree
    else:
        print("noneeeeee")
        

if __name__ == '__main__':
    dataList = []
    f = open('dblp_1L.json', encoding="utf8")
    count = 0
    Bmain = BTree(5)
    for line in f:
        data = json.loads(line)
        dataList.append(data)
    for data in dataList:
        print("/\\\\\\\\\\\\\\\\\\\\\/")
        count = count + 1
        if(count<2):
            for key, value in data.items():
                insertToBTree(Bmain, count, key, value)
            Bmain.printTree(Bmain.root)
        else:
            break




    # Bmain = BTree(5)
    # for key, value in data.items():
    #     count = count + 1
    #     print("Key", key, "type", type(value))
    #     Bmain.insert_(key, count)
        
    # Bmain.printTree(Bmain.root)

