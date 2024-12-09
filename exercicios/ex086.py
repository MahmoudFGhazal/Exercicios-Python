n = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for x in range(0, 3):
        n[x][c] = int(input(f"Digite para [{c}, {x}]: "))
print("-"*30)
for c in range(0,3):
    for x in range(0,3):
        print(f"[{n[x][c]:^5}]", end="")
    print()
