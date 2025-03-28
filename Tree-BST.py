class Node:
    def __init__(my,key=0):
        my.data=key
        my.left=None
        my.right=None

class BSTree:
    def __init__(my):
        my.root=None
    
    def insert_Rec(my,root,key):
        if root==None:
            return Node(key)
        if root.data > key:
            root.left=my.insert_Rec(root.left,key)
        else:
            root.right=my.insert_Rec(root.right,key)
        return root
    
    def insert(my,key):
        my.root=my.insert_Rec(my.root,key)

    def inorder(my,root):
        if root==None:
            return
        my.inorder(root.left)
        print(root.data,end=" ")
        my.inorder(root.right)

    def preorder(my,root):
        if root==None:
            return 
        print(root.data,end=" ")
        my.preorder(root.left)
        my.preorder(root.right)

    def postorder(my,root):
        if root==None:
            return
        my.postorder(root.left)
        my.postorder(root.right)
        print(root.data,end=" ")

if __name__=='__main__':
    BST1=BSTree()
    BST1.insert(6)
    BST1.insert(4)
    BST1.insert(8)
    BST1.insert(5)
    BST1.insert(10)
    BST1.insert(7)
    BST1.inorder(BST1.root)
    print()
    BST1.preorder(BST1.root)
    print()
    BST1.postorder(BST1.root)
    print()