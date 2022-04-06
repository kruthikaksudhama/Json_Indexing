import json
from bplustree import BplusTree

#Parameters
keys_per_node=3

class idxNode:  #Consists of array of B+ trees of children

    def __init__(self, keys_per_node):
        self.children = BplusTree(keys_per_node)
        self.array_children = BplusTree(keys_per_node)
        self.value_tree = BplusTree(keys_per_node)

class Path:

    def __init__(self):
        self.arr_idx = []
        self.attr_path = []


# Todo: differentiate between numbers and strings in path
def search_path(path, node):     #Check if there is an existing node at the given path

    for attr in path:
        #Find using B+ tree search
        curr = node.search(attr)   #Modify
        if not len(curr):
            return None

    return curr

def process_document(d, path, index):

    for (key, value) in d:

        path.attr_path.append(key)
        if type(value) == dict:     #Normal internal node

            if not len(path) or type(path[-1]) == tuple:
                arr_child =  index.arr_children.search(key)
                if not arr_child:
                    arr_child = idxNode()

                arr_child = process_document(value, path, arr_child)
                index.arr_children.insert(key, arr_child)
            else:
                child =  index.children.search(key)
                if not child:
                    child = idxNode()

                child = process_document(value, path, child)
                index.arr_children.insert(key, child)

        elif type(value) == list:

            index = process_arr(value, path, index)

        else:

            index.value_tree.insert(value, path)

    return index

def process_arr(arr, path, index):

    for arr_idx, elem in enumerate(arr):   #Process each document

        level = len(path.attr_path)
        path.arr_idx.append((arr_idx, level))
        if type(elem) == dict:

            index = process_document(elem, path, index)

        if type(elem) == list:

            index = process_arr(elem, path, index)

        else:

            index.value_tree.insert(elem, path)
        
    return index

if __name__ == '__main__':

    documents=[]
    num_docs = 1
    f = open('../Dataset/dblp_1L.json')
    for line in f:
        if len(documents) >= num_docs:
            break
        d = json.loads(line)
        documents.append(d)
    f.close()


    index = process_arr(documents, Path(), idxNode(keys_per_node))

