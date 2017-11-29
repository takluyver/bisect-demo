"""Squaring tool"""
import argparse

__version__ = '0.1'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('n', help='Number to square', type=int)
    args = ap.parse_args()

    n = args.n

    ref = 0
    for i in range(n):
        ref += n
    print(ref)

if __name__ == '__main__':
    main()
