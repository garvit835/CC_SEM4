class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_manual(self, root):
        if root is None:
            val = int(input("Enter node value: "))
            return Node(val)

        ch = input(f"Insert left child of {root.data}? (y/n): ")
        if ch.lower() == 'y':
            root.left = self.insert_manual(root.left)

        ch = input(f"Insert right child of {root.data}? (y/n): ")
        if ch.lower() == 'y':
            root.right = self.insert_manual(root.right)

        return root

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

def are_mirror(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return (a.data == b.data and
            are_mirror(a.left, b.right) and
            are_mirror(a.right, b.left))

# Menu-driven program
if __name__ == "__main__":
    tree1 = BinaryTree()
    tree2 = BinaryTree()

    while True:
        print("\n--- Mirror Tree Checker ---")
        print("1. Create Tree 1")
        print("2. Create Tree 2")
        print("3. Display Tree 1 (Inorder)")
        print("4. Display Tree 2 (Inorder)")
        print("5. Check if Tree 1 and Tree 2 are Mirror Images")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Creating Tree 1:")
            tree1.root = tree1.insert_manual(tree1.root)
        elif choice == '2':
            print("Creating Tree 2:")
            tree2.root = tree2.insert_manual(tree2.root)
        elif choice == '3':
            print("Tree 1 (Inorder):")
            tree1.inorder(tree1.root)
            print()
        elif choice == '4':
            print("Tree 2 (Inorder):")
            tree2.inorder(tree2.root)
            print()
        elif choice == '5':
            if are_mirror(tree1.root, tree2.root):
                print("YES! Tree 1 and Tree 2 are mirror images.")
            else:
                print("NOPE! Tree 1 and Tree 2 are NOT mirror images.")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
