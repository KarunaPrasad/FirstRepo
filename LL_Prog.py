class LL:
    head = None
    tail = None
    def __init__(self,val=0):
        if(LL.head == None):
            LL.head = LL.tail = self
            self.val = val
            print(self.val)
            self.next = None
        else:
            LL.tail.next = self
            self.next = None
            self.val = val
            print(self.val)
    def printLL(self):
        temp=LL.head
        while(temp.next != None):
            print(str(temp.val) + "\n")
            temp= temp.next
node1 = LL()
v = "Y"
while (v != "N"):
    v= input("Please enter new node value:(Press 'N' for exit)")
    obj = LL(v)
    print(v)

obj.printLL()

