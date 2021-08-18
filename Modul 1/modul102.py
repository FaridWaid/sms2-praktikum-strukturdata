def mat (a):
    jumlah = 0
    for i in range(1,a+1):
        jumlah = jumlah +((3*i) +4)
    jumlahtotal= jumlah / (5*a)
    return jumlahtotal
print (mat(1))
print (mat(2))
print (mat(3))
print (mat(5))
print (mat(100))
