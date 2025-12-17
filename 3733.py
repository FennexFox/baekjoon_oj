while True:
    try:
        people, shares = map(int, input().split())
        print(shares // (people + 1))
    except:
        break