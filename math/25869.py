w, h, d = map(int, input().split())
print(max((w-2*d),0)*max(h-2*d,0))