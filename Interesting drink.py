n = int(input())
prices =list(map(int,input().split()))
q = int(input())
days = [int(input()) for i in range(q)]

prices.sort()

def binary_search(prices,m):
   left,right = 0,len(prices)-1
   while left <= right:
      mid = (left+right)//2
      if prices[mid] <= m:
         left = mid+1
      else:
         right = mid-1
   return left 

results =[]
for m in days:
   count = binary_search(prices,m)
   results.append(count)
print("\n".join(map(str, results)))
