list=[-71,-10,56,24,-90,43,-16]

def numbers(num):
  p=0
  n=0
  for j in num:
      if(j>0):
        p=p+1
      else:
        n=n+1
  print("Number of positive numbers:",p)
  print("Number of negative number:",n)
numbers(list)
