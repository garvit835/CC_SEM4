class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def get_length(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length

def find_merge_point(head1, head2):
    len1 = get_length(head1)
    len2 = get_length(head2)

    # Advance the longer list's pointer by the difference in length
    if len1 > len2:
        for _ in range(len1 - len2):
            head1 = head1.next
    else:
        for _ in range(len2 - len1):
            head2 = head2.next

    # Move both together until we find the merge point
    while head1 and head2:
        if head1 == head2:
            return head1
        head1 = head1.next
        head2 = head2.next
    return None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return new_node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Menu-driven program
if __name__ == "__main__":
    list1 = LinkedList()
    list2 = LinkedList()
    merged_part = None

    while True:
        print("\n--- Find Merge Point of Two Linked Lists ---")
        print("1. Add node to List 1")
        print("2. Add node to List 2")
        print("3. Create common merged part")
        print("4. Attach merged part to both lists")
        print("5. Display List 1")
        print("6. Display List 2")
        print("7. Find merge point")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            val = int(input("Enter value to insert into List 1: "))
            list1.append(val)

        elif choice == '2':
            val = int(input("Enter value to insert into List 2: "))
            list2.append(val)

        elif choice == '3':
            merged_part = LinkedList()
            count = int(input("How many nodes in merged part? "))
            for i in range(count):
                val = int(input(f"Enter value {i+1}: "))
                merged_part.append(val)
            print("Created merged segment.")

        elif choice == '4':
            if not merged_part or not merged_part.head:
                print("Merged part is empty.")
            else:
                # Attach to end of List 1
                cur = list1.head
                if cur:
                    while cur.next:
                        cur = cur.next
                    cur.next = merged_part.head
                else:
                    list1.head = merged_part.head

                # Attach to end of List 2
                cur = list2.head
                if cur:
                    while cur.next:
                        cur = cur.next
                    cur.next = merged_part.head
                else:
                    list2.head = merged_part.head
                print("Attached merged part to both lists.")

        elif choice == '5':
            print("List 1:")
            list1.display()

        elif choice == '6':
            print("List 2:")
            list2.display()

        elif choice == '7':
            merge_node = find_merge_point(list1.head, list2.head)
            if merge_node:
                print(f"Merge point found at node with value: {merge_node.data}")
            else:
                print("No merge point found.")

        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
