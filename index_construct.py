import json
from bplustree import BplusTree

#Parameters
keys_per_node=3

class idxNode:  #Consists of array of B+ trees of children

    def __init__(self):
        self.children = []
        self.value_tree = BplusTree(keys_per_node)
        self.isArray = False

def search_path(path, node):     #Check if there is an existing node at the given path

    for attr in path:
        #Find using B+ tree search
            
        

def create_index(documents, path):

    index = idxNode()

    for i, d in enumerate(documents):

        if type(d) == dict:     #Normal internal node
            print('Dict')

        elif type(d) == list:   #Array node
            print('List')

        else:   #Leaf node
            idx = list(filter(lambda x: type(x) == int, path))
            idx = idx.append(i)
            value_tree.insert(d, idx)

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

    index = 

