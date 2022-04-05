import json
import pathlib

documents=[]
num_docs = 3
f = open(pathlib.Path('../Data/dblp_1L.json'))

for line in f:
    if len(documents) >= num_docs:
        break
    documents.append(json.loads(line))

print(json.dumps(documents, indent=3), sep="\n"*2)
f.close()