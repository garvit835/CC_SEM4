class MinStack:
    def __init__(self, capacity):
        self.stack = []
        self.min_stack = []
        self.capacity = capacity

    def is_full(self):
        return len(self.stack) == self.capacity

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, value):
        if self.is_full():
            print("⚠️ Stack Overflow! Cannot push", value)
            return
        self.stack.append(value)
        # Push to min_stack if it's the smallest so far
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
        print(f"✅ Pushed: {value}")

    def pop(self):
        if self.is_empty():
            print("⚠️ Stack Underflow! Nothing to pop.")
            return None
        popped = self.stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()
        print(f"🗑️ Popped: {popped}")
        return popped

    def top(self):
        if self.is_empty():
            print("⚠️ Stack is empty. No top element.")
            return None
        print(f"🔝 Top Element: {self.stack[-1]}")
        return self.stack[-1]

    def get_min(self):
        if not self.min_stack:
            print("⚠️ Stack is empty. No min element.")
            return None
        print(f"📉 Min Element: {self.min_stack[-1]}")
        return self.min_stack[-1]

    def display(self):
        if self.is_empty():
            print("📭 Stack is empty.")
        else:
            print("📦 Stack from top to bottom:")
            for i in reversed(self.stack):
                print(i)

# 🔧 Test the MinStack
if __name__ == "__main__":
    size = int(input("Enter the capacity of the stack: "))
    s = MinStack(size)

    while True:
        print("\nChoose operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Top")
        print("4. Get Min")
        print("5. Display Stack")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            val = int(input("Enter value to push: "))
            s.push(val)
        elif choice == 2:
            s.pop()
        elif choice == 3:
            s.top()
        elif choice == 4:
            s.get_min()
        elif choice == 5:
            s.display()
        elif choice == 6:
            print("👋 Exiting...")
            break
        else:
            print("⚠️ Invalid choice! Try again.")