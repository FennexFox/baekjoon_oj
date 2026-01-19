# Z (https://www.acmicpc.net/problem/1074)
# tier: Gold 5
# tags: Divicde and Conquer, Recursive

n, r, c = map(int, input().split())
side, steps = 2**n, 0

def check_quadrants(side, r, c):
    half = side//2
    quadrant = 0
    if r >= half:
        quadrant += 2
    if c >= half:
        quadrant += 1
    return quadrant * (half**2), half, quadrant

while side > 1:
    area, side, quadrant = check_quadrants(side, r, c)
    steps += area
    
    if quadrant >= 2:
        r -= side
    if quadrant % 2 == 1:
        c -= side

print(steps)