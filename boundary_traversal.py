class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, val):
        if root is None:
            return Node(val)
        if val < root.data:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        return root

    def print_boundary(self, root):
        if root is None:
            return

        print("Boundary traversal:")

        print(root.data, end=" ")  # Step 1: Print root

        # Step 2: Print left boundary (excluding leaves)
        self.print_left_boundary(root.left)

        # Step 3: Print all leaf nodes
        self.print_leaves(root.left)
        self.print_leaves(root.right)

        # Step 4: Print right boundary in reverse (excluding leaves)
        self.print_right_boundary(root.right)

    def print_left_boundary(self, node):
        if node:
            if node.left:
                print(node.data, end=" ")
                self.print_left_boundary(node.left)
            elif node.right:
                print(node.data, end=" ")
                self.print_left_boundary(node.right)

    def print_right_boundary(self, node):
        if node:
            if node.right:
                self.print_right_boundary(node.right)
                print(node.data, end=" ")
            elif node.left:
                self.print_right_boundary(node.left)
                print(node.data, end=" ")

    def print_leaves(self, node):
        if node:
            self.print_leaves(node.left)
            if node.left is None and node.right is None:
                print(node.data, end=" ")
            self.print_leaves(node.right)

# Menu-driven interaction
if __name__ == "__main__":
    tree = BST()

    while True:
        print("\n--- Boundary Traversal of BST ---")
        print("1. Insert node")
        print("2. Perform boundary traversal")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            val = int(input("Enter value to insert: "))
            tree.root = tree.insert(tree.root, val)
        elif choice == '2':
            tree.print_boundary(tree.root)
            print()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
