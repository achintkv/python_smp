print('Enter the number n\n')
n=int(input())
a=n
i=n
i-=1
while i>0:
    a*=i
    i-=1
print('The Factorial of',n,'is',a)
