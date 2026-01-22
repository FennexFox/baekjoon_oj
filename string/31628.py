eggplants_h = [input().split() for _ in range(10)]
eggplants_v = [[eggplants_h[y][x] for y in range(10)] for x in range(10)]

for z in range(10):
    if len(set(eggplants_h[z])) == 1 or len(set(eggplants_v[z])) == 1:
        print(1)
        exit()

print(0)