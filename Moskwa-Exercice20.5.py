# -*- coding: utf-8 -*-
import math
import time
from random import randrange

def Horner (g,x,i):
#calcule les coefficients de Horner
    if i==0:
        return g[0]
    else:
        return Horner(g,x,i-1)*x+g[i]
        
def valeur(I,b):
#retourne l'entier dont l'ecriture est dans la base b
    h=list(reversed(I))
    return str(Horner(h,b,len(h)-1))

def pgcd(a,b):
#calcule de maniere recursive le pgcd de deux nombres
    r=a%b
    if r==0 :
        return b
    else:
        return pgcd (b,r)

def rBezout (r,u,v,i,pgcd):
#calcule les coefficients de bezout pour un vecteur de deux nombres demaniere recursive
    if r[-1] == pgcd:
        print r
        print u
        print v
        return
    else:
        r.append (r[i-1]-int(r[i-1]/r[i])*r[i])
        u.append (u[i-1]-int(r[i-1]/r[i])*u[i])
        v.append (v[i-1]-int(r[i-1]/r[i])*v[i])
        rBezout (r,u,v,i+1,pgcd)

def Bezout (r):
#renvoie le calcul les coefficients de bezout pour un vecteur de deux nombres
    _pgcd=pgcd(r[0],r[1])
    u=[1,0]
    v=[0,1]
    rBezout(r,u,v,1,_pgcd)
    print "Bezout:"+str(u[-1])+"x"+str(r[0])+"x"+str(r[1])+"="+str(pgcd(r[0],r[1]))
    print "u="+str(v[-1])
    print "r="+str(r[1])
    print "phi="+str(r[0])
    print u[-1]*r[0]+v[-1]*r[1]
    return [u[-1],v[-1]]
    
def getErathostene (k):
#Crible Erathostene pour l'identification de nombres premiers entre deux valeurs
    a=int(math.pow(2,k))
    b=int(math.pow(2,(k+1))+1)
    r=[]
    print"a="+str(a)+",b="+str(b)
    for i in range(a,b):
        pr=True
        for j in range (2,int(math.sqrt(i))+1):
            if i%j==0:
                pr=False
                break
        if pr:
            if len(r)<2:
                r.append(i)
            else:
                return r
                break
                
def genCles(k):
#retourne un couple de couples (n,u),(n,u) de clés publiques et privées
    P=getErathostene(k)
    p=P[0]
    q=P[1]
    
    n=p*q
    Phi_n=n-(p+q)+1
    
    a=(p-1)*(q-1)
    b=randrange(p,2*p+1)
    t=Bezout([a,b])
    print "####"
    print t
    print "#### genCles"
    r=t[1]
    u=b
    print "r="+str(r)
    print "u="+str(u)
    print "n="+str(n)
    M=18877
    msg=divmod(M,n)[1]
    C=pow(msg,u,n)
    print "===> Message clear="+str(msg)
    print "===> Message crypt="+str(C)
    print "===> Message decrypt="+str(pow(C,r,n))

#exemple simple
p=3
q=5
u=3
r=27
M=18877
n=p*q
#b=randrange(1,p*10)
#Phi_n=n-(p+q)+1
#t=Bezout([Phi_n,b])
#C=prm(M,u,n)
msg=divmod(M,n)[1]
print "msg=",msg
C=pow(msg,u,n)


print "===> Message clear="+str(msg)
print "===> Message crypt="+str(C)
print "===> Message decrypt="+str(pow(C,r,n))


#Serie 1:
r=[33554467,33554473]
#u=[1,0]
#v=[0,1]
print "pgcd="+str(pgcd (r[0],r[1]))
t0=time.time()
Bezout(r)
t1=time.time()
print "total time="+str(t1-t0)

#Serie2:
print "###### EX 1"
print str(valeur([0,2,1],3))