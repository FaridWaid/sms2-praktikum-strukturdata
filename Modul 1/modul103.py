x=[2,1,5,6]
y=[6,7]
z=[3,7,9,0,2,4,6,2]
def jumlahlist (a,b):
    jumlah=[]
    if len(a) < len(b):
        for i in range (len(b)):
            a.append(0)
            jumlah.append(a[i]+b[i])
    elif len(a) > len (b):
        for i in range (len(a)):
            b.append(0)
            jumlah.append(a[i]+b[i])
    elif len(a)==len(b):
        for i in range(len(a)):
            jumlah.append(a[i]+b[i])
    return (jumlah)      

print (jumlahlist(x,y))
print (jumlahlist(x,z))
