n = int(input())
events = list(map(int, input().split()))

if len(events)==n:
   crimes =0
   Officers =0

   for event in events:
    if event > 0:
      Officers +=event
    elif event == -1:
      if Officers > 0:
        Officers -=1
      else:
        crimes +=1

   print(crimes)

