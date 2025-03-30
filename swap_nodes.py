class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

    def swap_pairs(self):
        if not self.head or not self.head.next:
            print("No pairs to swap.")
            return

        prev = None
        current = self.head
        self.head = current.next  # New head will be the second node

        while current and current.next:
            next_pair = current.next.next
            second = current.next

            # Swapping
            second.next = current
            current.next = next_pair

            if prev:
                prev.next = second

            # Move to the next pair
            prev = current
            current = next_pair

        print("Swapped nodes pairwise.")

# Menu-driven
if __name__ == "__main__":
    ll = LinkedList()

    while True:
        print("\n--- Pairwise Swap in Linked List ---")
        print("1. Add element")
        print("2. Display list")
        print("3. Swap nodes pairwise")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            val = int(input("Enter value to insert: "))
            ll.append(val)
        elif choice == '2':
            print("Linked List:")
            ll.display()
        elif choice == '3':
            ll.swap_pairs()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
