seconds = 0
time1, dmg1 = map(int, input().split())
time2, dmg2 = map(int, input().split())
time3, dmg3 = map(int, input().split())
health = int(input())

def get_gcd(num1, num2):
    num1, num2 = num2, num1 % num2
    if num2 == 0:
        return num1
    else:
        return get_gcd(num1, num2)

timestep = get_gcd(get_gcd(time1, time2), time3)

while health > 0:
    health -= dmg1 if not(seconds % time1) else 0
    health -= dmg2 if not(seconds % time2) else 0
    health -= dmg3 if not(seconds % time3) else 0
    seconds += timestep if health > 0 else 0

print(seconds)