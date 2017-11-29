"""Squaring tool"""
import argparse
import sys

__version__ = '0.1'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('n', help='Number to square')
    args = ap.parse_args()

    try:
        n = int(args.n)
    except ValueError:
        print(args.n, 'is not an integer')
        sys.exit(1)

    ref = 0
    for i in range(n):
        ref += n
    print(ref)

if __name__ == '__main__':
    main()
