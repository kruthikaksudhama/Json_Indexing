import json
from bplustree import BplusTree, Node

#Parameters
keys_per_node=3

class idxNode:  #Consists of array of B+ trees of children

    def __init__(self, keys_per_node):
        self.children = BplusTree(keys_per_node)
        self.array_children = BplusTree(keys_per_node)
        self.value_tree = BplusTree(keys_per_node)
        self.array_value_tree = BplusTree(keys_per_node)

class Path:

    def __init__(self):
        self.arr_idx = []
        self.attr_path = []

#Example of a path:
# Institution
# eg_path.attr_path = [college, students,  name, first_name]
# eg_path.arr_idx = [(7->arr_idx, 2->level), (), ..]

# process [Array school documemts] 
# while processing 7th documentat root:
#   attr_path= [nirf]
#   arr_idx=[(7, 0)]

def process_document(d, path, index):

    for (key, value) in d:

        path.attr_path.append(key)
        if type(value) == dict:     #Normal internal node

            if not len(path.attr_path) or  len(path.attr_path) == path.arr_idx[-1][1] == tuple:     #The document is part of an array
                res =  index.arr_children.search_val(key)
                if not len(res):
                    arr_child = idxNode()
                else:
                    arr_child= res[0]

                arr_child = process_document(value, path, arr_child)
                index.arr_children.insert(key, arr_child)
            else:                                                                                   #The document is a child of a document
                res =  index.children.search_val(key)
                if not len(res):
                    child = idxNode()
                else:
                    child = res[0]

                child = process_document(value, path, child)
                index.children.insert(key, child)

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

            index.array_value_tree.insert(elem, path)
        
    return index

def construct(file_path='./dblp_1L.json', num_docs=1):

    documents=[]
    f = open(file_path)
    for line in f:
        if(not len(line)):
            continue
        print(len(documents))
        print(line)
        if len(documents) >= num_docs:
            break
        d = json.loads(line)
        documents.append(d)
    f.close()

    index = process_arr(documents, Path(), idxNode(keys_per_node))
    return index

if __name__ == '__main__':

    file_path = '../Dataset/dblp_1L.json'
    index = construct(file_path, 5)
    print('Number of attributes in level 0 of index: ') #Use API to get number of (key, value) pairs

