
from index_construct import construct


def search_query(index, path, value):

    path = path.split('.')
    typ = 'arr'
    curr_node = index

    for x in path:

        if x == '$':
            typ = 'arr'
        else:

            if typ == 'arr':
                res = curr_node.arr_children.search(x)
            else:
                res = curr_node.children.search(x)

            if not len(res):
                return []

            typ = 'node'
            
    if typ == 'arr':
        return curr_node.arr_value_tree.search(value)
    else:
        return curr_node.value_tree.search(value)


if __name__ == '__main__':

    file_path = '../Dataset/dblp_1L.json'
    index = construct(file_path)

    query_path = input('Enter path separated by \'.\': ')
    value = input('Enter value: ')