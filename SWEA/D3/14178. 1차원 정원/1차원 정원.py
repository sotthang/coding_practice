import math
T = int(input())
for test_case in range(1, T + 1):
    n, d = map(int, input().split())
    print(f'#{test_case} {math.ceil(n/(2*d+1))}')