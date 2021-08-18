def binsearch(listData,key):
    for a in range (1,len(listData)):
        x = listData[a]
        b=a-1
        while b>=0 and x<=listData[b]:
            listData[b+1]=listData[b]
            b-=1
        listData[b+1]=x
        print(listData)
    found=False
    first= 0
    last=len(listData)-1
    more=[]
    tengah = int
    u = 0
    while first<=last and not (found):
        mid = (first+last)//2
        if listData[mid]==key:
            more.append(mid)
            found = True
            tengah = mid
        elif key>listData[mid]:
            first=mid+1
 
        elif key<listData[mid]:
            last=mid-1
    u +=1
    if found:
        count = 1
        check = True

        while check == True:
            if (tengah + count) <= (len(listData)-1):

                if listData[tengah] == listData[tengah + count] and listData[tengah] == listData[tengah - count] :
                    more.append(tengah + count)
                    more.append(tengah - count)
                    count += 1
                    
                elif listData[tengah] == listData[tengah + count] and listData[tengah] != listData[tengah - count] :
                    more.append(tengah + count)
                    count += 1

                elif listData[tengah] != listData[tengah + count] and listData[tengah] == listData[tengah - count] :
                    more.append(tengah - count)
                    count += 1
                    
                else:
                    check = False

            else:
                check = False

        print ("Posisi Data = ",sorted(more))
        print ("Jumlah Iterasi = ",count+u)

    else:
        print ("Posisi Data = Data tidak ada")
        print ("Jumlah Iterasi = ",count+u)

a=[12,2,4,5,6,8,23,54,21,54,67,54,25,78,90,54,65,65,12,65,78,54,54,54]
binsearch(a,12)
