import sys

N = int(input())
i, counter = 2, 1
while i*i <= N:
    if N%i == 0:
        counter = N//i
        break
    i += 1
print(N-counter)