import queues as que
def jumlahcpu(a):
    queue=que.Queue()
    d=0
    m=[]
    a=[]
    for i in range (cpu):
        matriks=[]
        for i in range (1):
            b=(str(input("Nama Proses: ")))
            a=(int(input("Waktu Proses : ")))
            matriks.append(b)
            matriks.append(a)
            m.append(matriks)
    a=list(reversed(m))
    queue = a
    print("Antrian Proses : ",queue)
    c=int(input("Waktu Proses CPU = "))
    print("Antrian Proses beserta Waktunya = ",queue)
    i=0
    while not que.isEmpty(queue):
        print("Iterasi ke-",i,":")
        if queue[len(queue)-1][1] - c > 0:
            d+= (queue[len(queue)-1][1] - c)
            print("     Proses",queue[len(queue)-1][0],"sedang diproses, dan sisa waktu proses",queue[len(queue)-1][0],"=",d)
            queue[len(queue)-1][1]=d
            que.enque(queue,que.deque(queue))
            print("     Data proses yang tersisa :",(queue))
            d=0
            i+=1
        elif queue[len(queue)-1][1] - c <= 0:
            print("     Proses",queue[len(queue)-1][0],"telah selesai diproses")
            que.deque(queue)
            print("     Data proses yang tersisa :",queue)
            i+=1
    return(" ")
cpu=int(input("Jumlah Proses yang akan dijadwal di CPU :"))
print(jumlahcpu(cpu))
    
