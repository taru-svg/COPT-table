import collections 
import itertools
from itertools import groupby



units=input("enter the units")
units=units.split(' ')
units = [float(i) for i in units]
print(units)



u=input("enter the for")
u=u.split(' ')
u=[float(i) for i in u]
print(u)

##for making list of sums after introducing Nth unit

f=[]

for i in range(len(units)):
    g=[]
    h=[]
    
    h.append(0)

    for j in range(i+1):
       
        g.append(units[j])
    
    for l in range(1,len(g)+1):
        x=lambda g,l:list(itertools.combinations(g,l))
        y=x(g,l)
        for b in range(len(y)):
            Sum=sum(y[b])
            h.append(Sum)
        res = [i[0] for i in groupby(h)]
    f.append(res)




#sum1=[[0,25],[0,25,50],[0,25,50,75,100]]




def p(x):
    if(x<=0):
        return(1)
    else:
        return(0)
        
        
for i in range(len(units)):
    c=units[i]
    sum2=f[i]
    x=[]
    
    for j in range(len(sum2)):
        #print(type(map1[sum2[j]]))
        
        if(j==0):
            x.append(1)
        elif(i==0 and j!=0):
            x.append((1-u[i])*p(sum2[j])+u[i]*p(sum2[j]-c))
            
        else:
            if(sum2[j]-c)<0:
                 map1[sum2[j]-c]=1
                 x.append((1-u[i])*map1[sum2[j]]+u[i]*map1[sum2[j]-c])
            else:
                x.append((1-u[i])*map1[sum2[j]]+u[i]*map1[sum2[j]-c])
            
         
    map1={}
    map1=collections.defaultdict(lambda:0)
    for k in range(len(sum2)):
        #if((sum2[k]-c)<0):
            #map1[sum2[k]-c]=1
        #else:
           
            map1[sum2[k]]=x[k]
    
    print(map1)

        
            

    
    
    