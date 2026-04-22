s = input()
o = sum(ord(x) for x in s)
print(chr(o//len(s)))