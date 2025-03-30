class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

# Menu-driven interaction
if __name__ == "__main__":
    bst = BST()

    while True:
        print("\n--- Build a Binary Search Tree (BST) ---")
        print("1. Insert element")
        print("2. Inorder Traversal (Left → Root → Right)")
        print("3. Preorder Traversal (Root → Left → Right)")
        print("4. Postorder Traversal (Left → Right → Root)")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            val = int(input("Enter value to insert: "))
            bst.root = bst.insert(bst.root, val)
        elif choice == '2':
            print("Inorder traversal:")
            bst.inorder(bst.root)
            print()
        elif choice == '3':
            print("Preorder traversal:")
            bst.preorder(bst.root)
            print()
        elif choice == '4':
            print("Postorder traversal:")
            bst.postorder(bst.root)
            print()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
