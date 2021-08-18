def unOrderedSearch2(listData,key):
    i=0
    more=[]
    found = False
    while i<len(listData):
        if listData[i]==key:
            more.append(i)
            found=True
        i+=1
    if found:
        print ("Posisi Data = ",more)
        print ("Jumlah Iterasi = ",i)
    else:
        print ("Posisi Data = Data tidak ada")
        print ("Jumlah Iterasi = ",i)

a=[54,30,25,73,12,15,2,30,25,12,45,25,100,34,5,30,6,7,25]
unOrderedSearch2(a,30)
