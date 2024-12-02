lucky_numbers =[]
stack =[4,7]

while stack:
  num = stack.pop(0)
  if num < 1000:
    lucky_numbers.append(num)
    stack.append(num*10+4)
    stack.append(num*10+7)

n = int(input())
is_almost_lucky = False
for  i in lucky_numbers :
  if n==i or n%i==0:
    is_almost_lucky =True
    break

if is_almost_lucky:
  print("YES")
else:
  print("NO")