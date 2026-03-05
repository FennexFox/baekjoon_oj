import sys
import math

input = sys.stdin.readline
print = sys.stdout.write
flooded_conv = 50 / math.pi # cache math.pi for faster calculations

while True:
    a, b = map(float, input().split())

    if a == 0 and b == 0:
        break

    area_conv = (a**2 + b**2) / 2 # divieded by pi to get the area in terms of flooded_conv
    hour = math.ceil(area_conv / flooded_conv)
        
    print(f"The property will be flooded in hour {hour}.\n")