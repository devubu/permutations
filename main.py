#!/usr/bin/python3
from itertools import permutations


def main():
    characters = "clear"
    all_permutations = [''.join(p) for p in permutations(characters)]

    for perm in all_permutations:
        print(perm)


if __name__ == "__main__":
    main()
