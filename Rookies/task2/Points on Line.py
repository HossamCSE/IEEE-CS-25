n, d = map(int, input().split())
points = list(map(int, input().split()))

total_groups = 0
j = 0

for i in range(n):
    while j < n and points[j] - points[i] <= d:
        j += 1
        count = j - i - 1  
        if count >= 2:
           total_groups += (count * (count - 1)) // 2  

print(total_groups)
