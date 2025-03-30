class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head or data < self.head.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def display(self):
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    h1 = l1.head
    h2 = l2.head

    while h1 and h2:
        if h1.data < h2.data:
            tail.next = h1
            h1 = h1.next
        else:
            tail.next = h2
            h2 = h2.next
        tail = tail.next

    # Attach remaining elements
    tail.next = h1 if h1 else h2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

# Menu-Driven
if __name__ == "__main__":
    list1 = LinkedList()
    list2 = LinkedList()

    while True:
        print("\n--- Merge Two Sorted Linked Lists ---")
        print("1. Add element to List 1")
        print("2. Add element to List 2")
        print("3. Display List 1")
        print("4. Display List 2")
        print("5. Merge both lists")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            val = int(input("Enter value to insert into List 1: "))
            list1.append(val)
        elif choice == '2':
            val = int(input("Enter value to insert into List 2: "))
            list2.append(val)
        elif choice == '3':
            print("List 1:")
            list1.display()
        elif choice == '4':
            print("List 2:")
            list2.display()
        elif choice == '5':
            print("Merged Sorted List:")
            merged = merge_sorted_lists(list1, list2)
            merged.display()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")
