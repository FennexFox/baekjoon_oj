import sys
print = sys.stdout.write

for n in range(11, 100):
    for d in range(11, 100):
        for b in range(1, 10):
            bn = int(str(n)+str(b))
            bd = int(str(b)+str(d))
            if bn/bd!=1 and bn/bd==n/d:
                print(f"{bn} / {bd} = {n} / {d}\n") 
            else:
                continue