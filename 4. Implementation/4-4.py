n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 현재 위치 방문 처리
graph[x][y] = 1
ans = 1

def turn_left(direction):
    direction -= 1
    if direction == -1: direction = 3
    return direction
# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

turn_time = 0
while 1:
    d = turn_left(d)
    turn_time += 1
    nx = x + dx[d]
    ny = y + dy[d]
    if graph[nx][ny] == 0:
        turn_time = 0
        graph[nx][ny] = 1
        ans += 1
        x, y = nx, ny
    
    if turn_time == 4:
        nx = x - dx[d]
        ny = x - dx[d]
        if graph[nx][ny] == 1:
            break

print(ans)