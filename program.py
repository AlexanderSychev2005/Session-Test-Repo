import time
n=9
fact=1
for i in range(2,n+1): 
  fact=fact*i 
print("The factorial of ",n," is: ",fact)





stroka = input("")

for slovo in stroka:
    print(slovo,end="  ", flush=True)
    time.sleep(1)

n=5
string="Hello World "
print(string * n)