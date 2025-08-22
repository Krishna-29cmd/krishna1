n=int(input("Enter a number:-"))
fact=1

print("the factorial of", n ," is ")

for i in range (1, n+1):
    fact = fact * i
  
print(fact)    