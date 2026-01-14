import sys

for line in sys.stdin:
    string = line.rstrip('\n')
    while "BUG" in string:
        string = string.replace("BUG", "")
    print(string)