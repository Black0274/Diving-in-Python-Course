import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if not os.path.isfile(storage_path):
    with open(storage_path, 'w') as f:
        pass
key = args.key

if args.val:
    value = args.val
    tup = (key, value)
    with open(storage_path, 'a') as f:
        f.write(json.dumps(tup))
        f.write('\n')
else:
    with open(storage_path, 'r') as f:
        lst = f.readlines()
        flag = False
        for line in lst:
            kw = json.loads(line)
            if kw[0] == key:
                if flag:
                    print(", ", end='')
                print(kw[1], end='')
                flag = True
        print()
