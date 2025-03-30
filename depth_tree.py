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

    def max_depth(self, node):
        if node is None:
            return 0
        left_depth = self.max_depth(node.left)
        right_depth = self.max_depth(node.right)
        return max(left_depth, right_depth) + 1

# Menu-driven program
if __name__ == "__main__":
    tree = BinaryTree()

    while True:
        print("\n--- Binary Tree Depth Finder ---")
        print("1. Insert node")
        print("2. Display inorder traversal")
        print("3. Find max depth of the tree")
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
            depth = tree.max_depth(tree.root)
            print(f"Maximum depth of the tree: {depth}")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
