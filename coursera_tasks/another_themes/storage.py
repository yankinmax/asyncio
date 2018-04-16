import argparse
import os
import tempfile
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

def storage_write(args):    
    with open(storage_path, 'w') as f:
        my_dict = dict()
        if args:
            my_dict[args.key] = args.value
            result = json.dumps(my_dict)
            return f.write(result)


def storage_read(args):    
    with open(storage_path, 'r') as f:
        data = f.read()
        print(data)
        loaded = json.loads(data)
        if args.key not in loaded:
            print(None)
        else:
            print(loaded.get(args.key))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is a PyMOTW sample program',)
    parser.add_argument("--key", dest='key', help="key in storage")
    parser.add_argument("--value", nargs='+', dest='value', help="value in storage")
    args = parser.parse_args()    
    if args.key and args.value:
        storage_write(args)
    elif args.key:
        storage_read(args)