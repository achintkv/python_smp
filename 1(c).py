c=input('c = ')
print(c)
b=c.find('+')
a=0
r='\0'
i='\0'
while a<b:
    r+=c[a]
    a+=1
print ('r =',r)    
a+=1
d=c.find('j')
while a<d:
    i+=c[a]
    a+=1
print ('i =',i)
