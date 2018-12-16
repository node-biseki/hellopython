#hello inori

from sys import argv

print('hello, {}'.format(args[1] if len(argv) == 2 else "world"))
