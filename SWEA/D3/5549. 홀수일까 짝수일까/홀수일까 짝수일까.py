T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case} Even') if int(input()) % 2 == 0 else print(f'#{test_case} Odd')