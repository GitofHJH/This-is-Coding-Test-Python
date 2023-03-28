n = input()

x, y = int(ord(n[0])) - 96, int(n[-1])

ans = 0
move = [(2, 1), (1, 2), (-2, 1), (1, -2), (2, -1), (-1, 2), (-2, -1), (-1, -2)]
for dx, dy in move:
    nx = x + dx
    ny = y + dy
    if nx <= 8 and nx >= 1 and ny <= 8 and ny >= 1:
        ans += 1

print(ans)