def faktor (a):
    hasil=[]
    for i in range (1,a+1):
        if a%i==0:
            hasil.append(i)

    return hasil
a=int(input('masukkan faktor berapa yang ingin dicari: '))
print(faktor(a))
