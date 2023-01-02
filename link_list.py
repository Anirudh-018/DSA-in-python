class node:
    def __init__(self,val=None):
        self.val=val
        self.next=None
class ll:
    def __init__(self):
        self.head=None
    def printer(self):
        print('printing link list')
        temp=self.head
        while temp.next!=None:
            print(temp.val)
            temp=temp.next
        print(temp.val)
    def insert_end(self,value):
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=node(value)
    def insert_front(self,value):
        temp=self.head
        self.head=node(value)
        self.head.next=temp
    def insert_mid(self,value,prev_val):
        temp=self.head
        while temp.next!=None:
            if temp.val==prev_val:
                succ=temp.next
                temp.next=node(value)
                temp.next.next=succ
                break
            else:
                temp=temp.next
        if temp.next==None:
            print("pos does not exist")
    def delete_node(self,value):
        if self.head==None:
            print("empty linked list")
            return
        temp=self.head
        if temp.val==value:
            list.head=temp.next
        prev=temp
        while temp.next!=None:
            prev=temp
            temp=temp.next
            if temp.val==value:
                prev.next=temp.next
def create_ll(value):
    root=node(value)
    list=ll()
    list.head=root
    root.next=None
    return list
print('enter choice')
a=int(input())
count=0
while a:
    if a==1:
        if count==0:
            print("enter value or root")
            value=int(input())
            list=create_ll(value)
            print('enter choice or 0')
            a=int(input())
            count+=1
        else:
            print("enter f,m,e and value")
            pos=input()
            value=int(input())
            if pos=='f':
                list.insert_front(value)
                print('enter choice or 0')
                a=int(input())
            elif pos=='m':
                print("enter prev val")
                mid=int(input())
                list.insert_mid(value,mid)
                print('enter choice or 0')
                a=int(input())
            else:
                list.insert_end(value)
                print('enter choice or 0')
                a=int(input())
    elif a==2:
        print("eneter value to be deleted")
        value=int(input())
        list.delete_node(value)
        print('enter choice or 0')
        a=int(input())
    elif a==3:
        list.printer()
        print('enter choice or 0')
        a=int(input())
    else:
        print("enter valid choice or 0")
        a=int(input())