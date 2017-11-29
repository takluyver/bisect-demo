import sys

def main():
    if len(sys.argv) < 2:
        print('Give me a number!')
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print(sys.argv[1], 'is not an integer')
        sys.exit(1)

    ref = 0
    for i in range(n):
        ref += n
    print(ref)

if __name__ == '__main__':
    main()
