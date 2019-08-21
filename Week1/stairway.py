import sys
inp = int(sys.argv[1])


for i in range(1, inp + 1):
    for j in range(inp - i):
        print(" ", end='')
    for k in range(i):
        print("#", end='')
    print()
