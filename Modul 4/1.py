def short(a,bubleshort,tipe):
    if bubleshort == "asc" and tipe == 1:
            for i in range (len(a)-1,0,-1):
                print ("Proses ke ",len(a)-i,"Jumlah Iterasi =",i)
                c = 1
                for j in range (i):
                    if a[j] > a[j+1]:
                        a[j],a[j+1] = a[j+1],a[j]
                    print (c,"=",a)
                    c=c+1
    elif bubleshort == "asc" and tipe == 2:
            for i in range (len(a)-1,0,-1):
                print ("Proses ke ",len(a)-i,"Jumlah Iterasi =",i)
                b = len(a)-1
                c = 1
                for j in range (i,0,-1):
                    if a[b] < a[b-1]:
                        a[b-1],a[b] = a[b],a[b-1]
                    print (c,"=",a)
                    b = b-1
                    c = c + 1
    elif bubleshort == "dsc" and tipe == 1:
            for i in range (len(a)-1,0,-1):
                print ("Proses ke ",len(a)-i,"Jumlah Iterasi =",i)
                b = len(a)-1
                c = 1
                for j in range (i,0,-1):
                    if a[b] > a[b-1]:
                        a[b-1],a[b] = a[b],a[b-1]
                    print (c,"=",a)
                    b = b - 1
                    c = c + 1
    elif bubleshort == "dsc" and tipe == 2:
            for i in range (len(a)-1,0,-1):
                print ("Proses ke ",len(a)-i,"Jumlah Iterasi =",i)
                c = 1
                for j in range (i):
                    if a[j] < a[j+1]:
                        a[j],a[j+1] = a[j+1],a[j]
                    print (c,"=",a)
                    c = c + 1
    else:
        print("Yang anda masukkan tidak sesuai")
    
a = [10,2,1,13,15,22,11,45]
bubleshort=str(input("Anda akan melakukan jenis sorting yang mana?(asc/dsc)"))
tipe=int(input("Anda akan menggunakan type apa?(1/2)"))
short(a,bubleshort,tipe)
    
