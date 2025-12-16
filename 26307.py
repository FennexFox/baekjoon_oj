for _ in range(int(input())):
    target = int(input())
    nums = ", ".join([f'{i} {target-i}' for i in range(1, (target+1)//2)])

    print(f"Pairs for {target}: {nums}")