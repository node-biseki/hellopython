import sys

args = sys.argv
if len(args) != 2 :
    args.insert(1, 'world') 

print('hello, {}'.format(args[1]))