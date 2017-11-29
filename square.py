import sys
if len(sys.argv) < 2:
    print('Give me a number!')
    sys.exit(1)

n = int(sys.argv[1])
print(n * n)
