class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if root is None:
            return Node(value)
        if value < root.data:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
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

# Menu-driven interface
if __name__ == "__main__":
    tree = BinaryTree()

    while True:
        print("\n--- Tree Traversals: Inorder, Preorder, Postorder ---")
        print("1. Insert node")
        print("2. Inorder Traversal (Left → Root → Right)")
        print("3. Preorder Traversal (Root → Left → Right)")
        print("4. Postorder Traversal (Left → Right → Root)")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            val = int(input("Enter value to insert: "))
            tree.root = tree.insert(tree.root, val)
        elif choice == '2':
            print("Inorder traversal:")
            tree.inorder(tree.root)
            print()
        elif choice == '3':
            print("Preorder traversal:")
            tree.preorder(tree.root)
            print()
        elif choice == '4':
            print("Postorder traversal:")
            tree.postorder(tree.root)
            print()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
