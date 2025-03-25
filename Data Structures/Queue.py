class Node:
    def __init__(my,key):
        my.data=key
        my.next=None

class Queue:
    def __init__(my):
        my.front=None
        my.rear=None
        my.length=0
    
    def enqueue(my,key):
        node=Node(key)
        if my.front==None:
            my.front=node
            my.rear=my.front
        else:
            my.rear.next=node
            my.rear=node
        my.length+=1
        return

    def dequeue(my):
        if my.length!=0:
            temp=my.front
            my.front=my.front.next
            my.length-=1
        del temp
        if my.front==None or my.front.next==None:
            my.rear=my.front
        return

    def peek(my) -> int:
        if my.length>0:
            return my.front.data
    
    def print_queue(my):
        temp=my.front
        while temp!=None:
            print(temp.data,end=' ')
            temp=temp.next
        return
    
if __name__=='__main__':
    Q1=Queue()
    Q1.enqueue(56)
    Q1.enqueue(6)
    Q1.enqueue(76)
    Q1.print_queue()
    print()
    Q1.dequeue()
    Q1.print_queue()
    print()