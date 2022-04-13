import json
from bplustree import BplusTree

#Parameters
keys_per_node=3

# name_table  stores a tuple: (name, level, value_tree/None)
# name_leaf_hm hashes leaves to point to list of name_table entries

#liteindex_search_name
def liteindex_search_name(n_table1, pt_idx1, key1):  #Searches name table for the attribute, returns position

    i=pt_idx1
    found = False
    l_max = n_table1[i][1]
    while i<len(n_table1) and n_table1[i][1]<l_max :

        if n_table1[i][0] == key1:
            found= True
            break
    
    return found, i

def check_parent(table, h_idx, pt_idx):     #Check if an attribute at a specific index is at the right path

    i=h_idx
    if pt_idx>len(table):
        return False
        
    while i>=0 and table[i][1]>table[pt_idx][1]:
        i-=1
        
    if i==pt_idx:
        return True

def liteindex_doc_dfs(d, d_id, n_table, nleaf_hm, pt_idx=0):

    if type(d) == dict:

        #Parse through attributes
        for key, value in d:

            #Process value
            if type(value) == dict:
                #Search for attribute in name table
                found, idx = liteindex_search_name(n_table, pt_idx, key)
                if found:
                    n_table, nleaf_hm = liteindex_doc_dfs(value, d_id, n_table, nleaf_hm, idx)
                else:
                    _, pt_level, _ = n_table[pt_idx]
                    n_table.insert(idx, (key, pt_level+1, None))

            elif type(value) == list:
                print('Array cannot be processed by liteindex')
                exit(0)

            else:
                #Check if attribute already exists
                found = False
                if nleaf_hm.has_key(key):
                    hits = nleaf_hm[key]
                    for h in hits:
                        if check_parent(n_table, h, pt_idx):     #Check if its chain of ancestors is the same
                            found = True
                            n_table[h][2] = n_table[h][2].insert(value, d_id)

                            break

                if not found:
                    found, idx = liteindex_search_name(n_table, pt_idx, key)    #To get the index where the new entry shuold be  inserted
                    assert not found
                    bptree = BplusTree(keys_per_node).insert(value, d_id)
                    n_table.insert(idx, (key, pt_level+1, bptree))    
                    nleaf_hm[key] = list([key])     #Inserting into hash map

def litendex_construct(file_path='../Dataset/dblp_1L.json', num_docs=1):

    documents=[]
    f = open(file_path)
    for line in f:
        if len(documents) >= num_docs:
            break
        d = json.loads(line)
        documents.append(d)
    f.close()

    #Return index after constructing index
    return index

if __name__ == '__main__':

    file_path = '../Dataset/dblp_1L.json'
    index = litendex_construct(file_path)

    #Check if construted properly