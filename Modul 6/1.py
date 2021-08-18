class Node:
    #constructor
    def __init__(self,item):
        self.data=item
        self.next=None
    #get_set
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,item):
        self.data=item
    def setNext(self,pt):
        self.next=pt


class LinkedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        return self.head==None
    def addNode(self,item):
        temp=Node(item)
        temp.setNext(self.head)
        self.head=temp
    def size(self):
        current=self.head
        count=0
        while current!=None:
            count+=1
            current=current.getNext()
        return count
    def search(self,item):
        curent = self.head
        found = False
        while curent != None and not found:
            if curent.getData() == item:
                found = True
            else:
                curent = curent.getNext()
        return found
    def display(self):
        curent = self.head
        while curent != None:
            print(curent.getData())
            curent = curent.getNext()



mylist=LinkedList()
mylist.addNode(45)
mylist.addNode(34)
mylist.addNode(70)
mylist.addNode(84)
mylist.addNode(97)
mylist.display()

