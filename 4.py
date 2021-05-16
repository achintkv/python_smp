print('Enter the number\n')
n=int(input())
a=0
b=1
c=0
print('The fibonacci series upto',n,'is')
print(a)
print(b)
while c<=n:
    c=a+b
    if c<=n:
        print(c)
    a=b
    b=c