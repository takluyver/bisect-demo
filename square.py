import sys
if len(sys.argv) < 2:
    print('Give me a number!')
    sys.exit(1)

if not (sys.argv[1].isdigit() or (sys.argv[1].startswith('-') and sys.argv[1][1:].isdigit())):
    print(sys.argv[1], 'is not an integer')
    sys.exit(1)

n = int(sys.argv[1])
ref = 0
for i in range(n):
    ref += n
print(ref)
