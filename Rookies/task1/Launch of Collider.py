n = int(input())
dir = input().strip()
pos = list(map(int, input().strip().split()))

times = []
for i in range(len(dir) - 1):
    if dir[i] == "R" and dir[i + 1] == "L":
        t = (pos[i + 1] - pos[i]) / 2
        times.append(t)

if times:
    print(int(min(times)))
else:
    print(-1)
