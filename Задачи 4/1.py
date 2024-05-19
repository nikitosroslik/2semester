import math
import random 
a='Саня'
cnd = 0
a1=a
m=[]
ans=[]
while True:
    for i in range (len(a)):
        y=random.choice(a)
        m.append(y)
        a=list(a)
        a.remove(y)
        a="".join(a)
    cnd+=1
    a=a1
    if  "".join(m) not in ans:
        ans.append("".join(m))
    m=[]
    if len(ans) == math.factorial(len(a)) :
        break
print(ans)
