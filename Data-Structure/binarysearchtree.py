class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(root, key):
        head=root
        while head!=None:
            if head.key < key:
                if head.right is None:
                    n=Node(key)
                    head.right=Node
                    return root
                head=head.right
            if head.key > key:
                if head.left is None:
                    n=Node(key)
                    head.left=Node
                head=head.left
                return root

    # Find the inorder successor
    def minValueNode(node):
        current = node

        # Find the leftmost leaf
        while(current.left is not None):
            current = current.left

        return current

    # Deleting a node
    def deleteNode(root, key):
        if root is None:
            return root

        # Find the node to be deleted
        if key < root.key:
            root.left = deleteNode(root.left, key)
        elif(key > root.key):
            root.right = deleteNode(root.right, key)
        else:
        # If the node is with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # If the node has two children,
            # place the inorder successor in position of the node to be deleted
            temp = minValueNode(root.right)
            root.key = temp.key

            # Delete the inorder successor
            root.right = deleteNode(root.right, temp.key)

        return root

    def inorderTraversal(self,root):
        if root is None:
            return None

        inorderTraversal(root.left)
        print(root.key)
        inorderTraversal(root.right)

    def preOrderTraversal(self,root):
        if root is None:
            return None

        print(root.key)
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)

    def postOrderTraversal(self,root):
        if root is None:
            return None

        postOrderTraversal(root.left)
        postOrderTraversal(root.right)
        print(root.key)
