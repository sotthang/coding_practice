import sys

for x in range(1, int(sys.stdin.readline())+1):
    a, b = map(int, sys.stdin.readline().split())
    print(f'Case #{x}:', a+b)