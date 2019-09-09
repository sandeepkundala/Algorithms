# compute 3a^(n/2) non recursively with complexity of O(lg(n))
n = int(input("Enter n:"))
a = int(input("Enter a:"))
res = 1
number = 3*a
print("Actual result:",number**(n/2))
if n==2:
  print("Computation Result:",number)
else:
  power = int(n/2)
  while (power>0):
    if((power & 1)==1):
      res = res*number
    power = power >> 1
    number *= number
  if(n%2==0):
    print("Computation Result:",res)
  else:
    number = 3*a
    root = number/2
    temp = 0
    while(root !=temp):
      temp = root
      root = (number/temp + temp)/2
    print(print("Computation Result:", res*root)
