# N-QUEENS 51:
from Programming.recursive.basic import result


def nc(l,r,c):
    i=c-1
    while i>=0:
        if l[r][i]=="Q":
            return False
        i-=1
    i=r-1
    j=c-1
    while i>=0 and j>=0:
        if l[i][j]=="Q":
            return False
        i-=1
        j-=1
    i=r+1
    j=c-1
    while i<r and j>=0:
        if l[i][j]=="Q":
            return False
        i+=1
        j-=1
    return True
def nqueens(n):
    l=[]
    for i in range (n):
        r=[]
        for j in range(n):
            r.append('.')
        l.append(r)
    res=[]
    nq(l,res,0)
    return res
def nq(l,res,col):
    if col==len(l):
        temp=[]
        for i in l:
            temp.append(str(i))
        res.append(temp)
        return
    for i in range(0,r):
        if nc(l,i,col):
            l[i][col]="Q"
            nq(l,res,col+1)
            l[i][col]="."

n=4
r=n
result=nqueens(n)
for i in result:
    for j in i:
        if j=="Q":
            print("Q",end=" ")
        else:
            print(".",end=" ")
    print()

