c, t = map(int, input().split())

cities = list(map(int,input().split()))
towers = list(map(int,input().split()))

if len(cities) == c and len(towers) == t:
      
    max_d =0
    cities.sort()
    towers.sort()

    for i in cities :
      for j  in towers:
        d = abs(i-j)
        if d > max_d:
          max_d = d

print(max_d)
