comp_price, comp_perf, me_price = map(int, input().split())
print(int(3 * comp_perf / comp_price * me_price))