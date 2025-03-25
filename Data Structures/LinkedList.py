class Node():
    def __init__(my,key):
        my.val=key
        my.next=None

class LinkedList():
    def __init__(my):
        my.head=None
        my.tail=my.head
        my.length=0

    # append as insert at end
    def append(my,key):
        new=Node(key)
        if my.head==None:
            my.head=new
            my.tail=new
            my.length=1
        else:
            my.tail.next=new
            my.tail=new
            my.length+=1
        return
    
    # prepend as insert at begin
    def prepend(my,key):
        new =Node(key)
        if my.head==None:
            my.head=new
            my.tail=new
            my.length=1
        else:
            new.next=my.head
            my.head=new
            my.length+=1
        return

    def print(my):
        if my.head==None:
            print("empty")
        else:
            temp=my.head
            while temp!=None:
                print(temp.val,end=' ')
                temp=temp.next
        return

    def insert(my,key,pos):
        if pos <= 1:
            my.prepend(key)
        elif pos >my.length:
            my.append(key)
        else:
            pass
            temp=my.head
            while pos > 2:
                temp=temp.next
                pos-=1
            new =Node(key)
            new.next=temp.next
            temp.next=new
        my.length+=1
        return
    
    def found(my,key) ->bool:
        present=False
        if my.head!=None:
            temp=my.head
            while (temp!=None):
                if temp.val==key:
                    present=True
                    break
                temp=temp.next
        return present

    def deleteByKey(my,key):
        if my.found(key):
            temp2=my.head
            if my.head.val==key:
                my.head=my.head.next
            else:
                temp=my.head
                while temp.next!=None and temp.next.val!=key:
                    temp=temp.next
                if temp.next:
                    temp2=temp.next
                    temp.next=temp2.next
                    if temp.next==None:
                        my.tail=temp
            del(temp2)
            my.length-=1
        else:
            print("Not Found")
        return

    def deleteByPosition(my,pos):
        temp2=my.head
        if pos > my.length:
            pos=my.length
        if pos <=1:
            my.head=my.head.next
        else:
            temp=my.head
            while pos > 2:
                temp=temp.next
                pos-=1
            temp2=temp.next
            temp.next=temp2.next
            del(temp2)
        my.length-=1
        return

if(__name__=='__main__'):
    LL=LinkedList()
    LL.append(5)
    LL.prepend(10)
    LL.append(6)
    LL.append(7)
    LL.prepend(10)
    LL.prepend(11)
    LL.insert(66,2)
    LL.print()
    print()
    LL.deleteByPosition(2)
    LL.print()

