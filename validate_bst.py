class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
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

    def is_valid_bst(self, node, min_val=float('-inf'), max_val=float('inf')):
        if node is None:
            return True
        if not (min_val < node.data < max_val):
            return False
        return (self.is_valid_bst(node.left, min_val, node.data) and
                self.is_valid_bst(node.right, node.data, max_val))

# Menu-driven interface
if __name__ == "__main__":
    tree = BinaryTree()

    while True:
        print("\n--- Binary Search Tree Validation ---")
        print("1. Insert element")
        print("2. Display inorder traversal")
        print("3. Check if tree is a valid BST")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            val = int(input("Enter value to insert: "))
            tree.root = tree.insert(tree.root, val)
        elif choice == '2':
            print("Inorder traversal:")
            tree.inorder(tree.root)
            print()
        elif choice == '3':
            if tree.is_valid_bst(tree.root):
                print("The tree is a VALID Binary Search Tree.")
            else:
                print("The tree is NOT a valid BST.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
