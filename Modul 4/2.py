def modified(a,bubleshort,tipe):
    if bubleshort == "asc" and tipe == 1:
            for i in range (len(a)-1,0,-1):
                print ("Proses ke ",len(a)-i,"Jumlah Iterasi =",i)
                c = 1
                for j in range (i):
                    if a[j] > a[j+1]:
                        a[j],a[j+1] = a[j+1],a[j]
                    print (c,"=",a)
                    c = c + 1
                tes = True
                for j in range (i):
                    if a[j]<= a[j+1]:
                        tes = tes and True
                    else:
                        tes = tes and False
                if tes:
                    return(a)
    elif bubleshort == "asc" and tipe == 2:
            for i in range (len(a)-1,0,-1):
                print ("Proses ke ",len(a)-i,"Jumlah Iterasi =",i)
                c = 1
                b = len(a)-1
                for j in range (i,0,-1):
                    if a[b] < a[b-1]:
                        a[b-1],a[b] = a[b],a[b-1]
                    print (c,"=",a)
                    c = c + 1
                    b = b-1
    elif bubleshort == "dsc" and tipe == 1:
            for i in range (len(a)-1,0,-1):
                print ("Proses ke ",len(a)-i,"Jumlah Iterasi =",i)
                c=1
                b = len(a)-1
                for j in range (i,0,-1):
                    if a[b] > a[b-1]:
                        a[b-1],a[b] = a[b],a[b-1]
                    print (c,"=",a)
                    c = c + 1
                    b = b - 1
                tes = True
                for j in range (i):
                    if a[b-j] <= a[(b-1)-j]:
                        tes = tes and True
                    else:
                        tes = tes and False
                if tes:
                    return(a)
    elif bubleshort == "dsc" and tipe == 2:
            for i in range (len(a)-1,0,-1):
                print ("Proses ke ",len(a)-i,"Jumlah Iterasi =",i)
                c = 1
                for j in range (i):
                    if a[j] < a[j+1]:
                        a[j],a[j+1] = a[j+1],a[j]
                    print (c,"=",a)
                    c = c + 1
                tes = True
                for j in range (i):
                    if a[j+1] <= a[j]:
                        tes = tes and True
                    else:
                        tes = tes and False
                if tes:
                    return(a)
    else:
        print("Yang anda masukkan tidak sesuai")

a = [100,34,1,7,2,4,6,77,4,54]
bubleshort=str(input("Anda akan melakukan jenis sorting yang mana?(asc/dsc)"))
tipe=int(input("Anda akan menggunakan type apa?(1/2)"))
modified(a,bubleshort,tipe)
    
    
    
