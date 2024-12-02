n = int(input())
s = list(map(int, input().split()))
if len(s) == n:
    max_height = max(s)
    min_height = min(s)
    max_index = s.index(max_height)
    min_index = len(s) - 1 - s[::-1].index(min_height)
    swaps = max_index + ((len(s) - 1) - min_index)
    if max_index > min_index:
        swaps -= 1
    print(swaps)