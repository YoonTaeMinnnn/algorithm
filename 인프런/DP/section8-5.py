n = int(input())
l = list(map(int, input().split()))
res = 0
dy = [0] * n
dy[0] = 1
for i in range(1,n):
  max = 0
  for j in range(i-1, 0, -1):
    if l[i] > l[j] and dy[j] > max:
      max = dy[j]
  dy[i] = max + 1
  if dy[i] > res:
    res = dy[i]

print(res)
