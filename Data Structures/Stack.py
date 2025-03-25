class Node:
    def __init__(my,key):
        my.data=key
        my.next=None

class Stack:
    def __init__(my):
        my.top=None
        my.length=0

    def push(my,key):
        new = Node(key)
        if my.top==None:
            my.top=new
        else:
            my.top.next=new
            my.top=new
        my.length+=1
        return

    def pop(my):
        if my.length!=0:
            temp=my.top
            my.top=my.top.next
        del temp
        my.length-=1
        return

    def peek(my) -> int:
        if my.length!=0:
            return my.top.data