from sys import stdin
from collections import deque
input = stdin.readline

dx = (2, 1, -1, -2, -2, -1, 1, 2)
dy = (1, 2, 2, 1, -1, -2, -2, -1)

def bfs():
    q = deque()
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            print(d[x][y])
            return
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not d[nx][ny]:
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))

for _ in range(int(input())):
    n = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    d = [[0]*n for _ in range(n)]
    bfs()