def prime(n):
  if (n==1):
    print("The number is prime number")
  elif (n==2):
      print("The number is prime number")
  else:
    for x in range(2,n):
      if(n % x==0):
        print("The number is not a prime number")
        return True
a=int(input("Enter a number:"))                       
prime(a)



