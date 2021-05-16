a=[]
n=int(input('Enter the number of elements -'))
i=0
print('Enter the Elements')
for i in range(0,n):
    b=int(input())
    i+=1
    a.append(b)
pos=0
neg=0
j=0
while j<n:
    if a[j]>0:
        pos+=a[j]
    else:
        neg+=a[j]
    j+=1
neg*=-1
if pos>neg:
    print ('POSITIVE')
elif neg>pos:
    print('NEGATIVE')
else:
    print('NEUTRAL')