# alternate uppercase and lowercase letters solution by gaurav nv

# the program should print alternate uppercase and lowercase by given pair value
# if 2 is the pair value then program prints 2 uppercase letters and then 2 lowercase letters alternatively
# till the input string has no uppercase and lowercase letters left
# i/p string = NoteBOOkPaper
# i/p pair = 2
# o/p N B o t O O e k a p e r

strg = input().strip() # input string 
k = int(input()) #no of uppercase nd lower case letter alertnatively
m = " ".join(c for c in strg if c.isupper()).split(" ");

n = " ".join(c for c in strg if c.islower()).split(" ");
if len(m)%2 != 0:
    m = m[0:-1]
    
elif len(n)%2 !=0:
    n = n[0:-1]
    
l = len(m) if m>n else len(n)

newarr = []
c=0
lc = 2
uc = 0
p = 0
q = 0
for i in range(0,l):

    if lc == 2 and uc<=k and (p!=len(m) or i<=len(m)):
        newarr.append(m[p])
        p+=1
        c+=1 
        uc+=1
        if uc == 2:
            lc = 0
    elif uc == 2 and lc<=k and (q!=len(m) or i<=len(n)):
        newarr.append(n[q])
        q+=1
        c+=1
        lc+=1
        if lc == 2:
            uc = 0
    else:continue

if p<len(m):
    newarr.extend(m[p:]) 
elif q<len(n):
    newarr.extend(n[q:])
    
print(" ".join(newarr))
