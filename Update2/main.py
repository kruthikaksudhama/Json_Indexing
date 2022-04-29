import json
from BplusTree import BTree, BNode
from tokenization import tokenization

def insertToBTree(tree, doc_num, key, value):

    tree.insert_(key, doc_num)

    if(type(value) == dict):
        for k, v in value.items():
            tree = tree.search(tree.root, key)
            insertToBTree(tree, doc_num, k, v)

    elif(type(value) == list):
        tree = tree.search(tree.root, key)
        for i in range(len(value)):
            tree.insert_(value[i], doc_num)

    elif(type(value) == str):
        print("calling here")
        tree = tree.search(tree.root, key)
        tree.insert_(value, doc_num)
        # keyword_str = tokenization(value)
        # keyword_extract = keyword_str.split(' ')
        # tree = tree.search(tree.root, key)
        # for i in range(len(keyword_extract)):
        #     tree.insert_(keyword_extract[i], doc_num)
    
    else:
        print("none")

# def search_val(value, treeList):
#     for tree in treeList:
#         child = tree.search(tree.root, value)
#         if(child ==None):
#             docList = 


# def search_(path, Btree):
#     chunks = path.split('/')
#     treeList = [Btree]
#     for chunk in chunks:
#         treeList = search_val(chunk, treeList)

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
        if(count<3):
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

