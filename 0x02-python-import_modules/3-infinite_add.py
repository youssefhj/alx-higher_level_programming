#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    it = 0
    for i in range(len(sys.argv) - 1):
        it = it + int(sys.argv[i + 1])
    print(it)
