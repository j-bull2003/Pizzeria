import sys
from collections import deque

# Read input from stdin
n, m = map(int, input().split())
pizzerias = []
for i in range(m):
  x, y, r = map(int, input().split())
  pizzerias.append((x, y, r))

# Initialize delivery counts for each block to 0
delivery_counts = [[0] * n for _ in range(n)]

# Iterate through each pizzeria and increment the delivery count
# for each block within its delivery range using BFS
for x, y, r in pizzerias:
  visited = [[False] * n for _ in range(n)]
  queue = deque([(x, y, 0)])
  while queue:
    i, j, d = queue.popleft()
    if d > r or visited[i][j]:
      continue
    visited[i][j] = True
    delivery_counts[i][j] += 1
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
      if 0 <= i + dx < n and 0 <= j + dy < n:
        queue.append((i + dx, j + dy, d + 1))

# Find the maximum delivery count
max_count = 0
for i in range(n):
  for j in range(n):
    max_count = max(max_count, delivery_counts[i][j])

# Print the maximum delivery count
print(max_count)