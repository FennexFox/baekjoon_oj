k = int(input())
ord_A = ord("A")

secret = input()
decoded = ""

def deocde(ch, p, k):
    decoded = ord(ch) - 3*p - k
    decoded = (decoded - ord_A) % 26 + ord_A
    return chr(decoded)

for digit, ch in enumerate(secret):
    decoded += deocde(ch, digit+1, k)

print(decoded)