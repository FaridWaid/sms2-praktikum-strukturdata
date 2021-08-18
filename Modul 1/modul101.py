def primaganjil (a):
    prima=[]
    ganjil=[]
    for i in range (1,a,2):
        if i == 1:
            ganjil.append(i)
        else:
            for j in range (2,i):
                if i %j == 0:
                    ganjil.append(i)
                    break
            else:
                prima.append(i)
    return prima, ganjil

a=int(input('masukkan batas bilangan: '))
print(primaganjil(a))
