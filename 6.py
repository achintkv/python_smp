print ('Enter a string -')
a=str(input())
i=0
b=[]
n=len(a)

for i in range(0,n):
    if a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u':
        b.append(a[i])

for i in range(0,n):
    if a[i]!='a' and a[i]!='e' and a[i]!='i' and a[i]!='o' and a[i]!='u':
        b.append(a[i])

c=b[0]
for i in range(1,n):
    c=c+b[i]
print ('The required string is',c)