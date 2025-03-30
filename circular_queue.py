class CircularQueue:
    def __init__(self, k):
        self.size = k
        self.queue = [None] * k
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full! Cannot enqueue.")
            return
        elif self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        print(f"Enqueued: {value}")

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty! Cannot dequeue.")
            return
        removed = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Dequeued: {removed}")

    def get_front(self):
        if self.front == -1:
            print("Queue is empty. No front element.")
            return
        print(f"Front element: {self.queue[self.front]}")

    def get_rear(self):
        if self.rear == -1:
            print("Queue is empty. No rear element.")
            return
        print(f"Rear element: {self.queue[self.rear]}")

    def display(self):
        if self.front == -1:
            print("Queue is empty.")
            return
        print("Queue elements:")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

# Menu-driven interaction
if __name__ == "__main__":
    size = int(input("Enter the size of the circular queue: "))
    cq = CircularQueue(size)

    while True:
        print("\n--- Circular Queue Operations ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Front")
        print("4. Rear")
        print("5. Display")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            val = int(input("Enter value to enqueue: "))
            cq.enqueue(val)
        elif choice == '2':
            cq.dequeue()
        elif choice == '3':
            cq.get_front()
        elif choice == '4':
            cq.get_rear()
        elif choice == '5':
            cq.display()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a number between 1-6.")
