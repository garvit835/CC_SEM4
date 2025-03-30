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

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def find_lca(self, root, n1, n2):
        if root is None:
            return None

        # If both values are smaller than root, LCA is in left
        if n1 < root.data and n2 < root.data:
            return self.find_lca(root.left, n1, n2)

        # If both values are greater than root, LCA is in right
        if n1 > root.data and n2 > root.data:
            return self.find_lca(root.right, n1, n2)

        # One value on each side (or one matches root), root is LCA
        return root

# Menu-driven interaction
if __name__ == "__main__":
    tree = BST()

    while True:
        print("\n--- Lowest Common Ancestor (LCA) in BST ---")
        print("1. Insert node")
        print("2. Inorder traversal")
        print("3. Find LCA of two nodes")
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
            if not tree.root:
                print("Tree is empty.")
            else:
                n1 = int(input("Enter first node value: "))
                n2 = int(input("Enter second node value: "))
                lca_node = tree.find_lca(tree.root, n1, n2)
                if lca_node:
                    print(f"LCA of {n1} and {n2} is: {lca_node.data}")
                else:
                    print("LCA not found (check if nodes exist).")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")
