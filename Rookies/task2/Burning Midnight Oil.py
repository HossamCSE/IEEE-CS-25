def can_write(v, n, k):
    total = 0
    current = v
    while current > 0:
        total += current
        current //= k 
        if total >= n:
            return True
    return total >= n

n, k = map(int, input().split())

low, high = 1, n
result = n

while low <= high:
    mid = (low + high) // 2
    if can_write(mid, n, k):
        result = mid
        high = mid - 1  
    else:
        low = mid + 1  
        
print(result)
