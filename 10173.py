import sys
input = sys.stdin.readline
print = sys.stdout.write

string = input().strip()
while string != "EOI":
    print("Found\n" if "nemo" in string.lower() else "Missing\n")
    string = input().strip()