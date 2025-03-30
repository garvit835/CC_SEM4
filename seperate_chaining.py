class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return sum(ord(ch) for ch in str(key)) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        # Check if key already exists, update it
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                print(f"Updated key '{key}' with value '{value}' at index {index}.")
                return
        # Else, insert new key-value
        self.table[index].append((key, value))
        print(f"Inserted key '{key}' with value '{value}' at index {index}.")

    def delete(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                print(f"Deleted key '{key}' from index {index}.")
                return
        print(f"Key '{key}' not found. Nothing to delete.")

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                print(f"Found key '{key}' at index {index} with value: {v}")
                return v
        print(f"Key '{key}' not found.")
        return None

    def display(self):
        print("Hash Table Contents:")
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")

# Menu-driven interface
if __name__ == "__main__":
    ht = HashTable()

    while True:
        print("\n--- Hash Table with Separate Chaining ---")
        print("1. Insert key-value pair")
        print("2. Delete key")
        print("3. Search key")
        print("4. Display hash table")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            key = input("Enter key: ")
            value = input("Enter value: ")
            ht.insert(key, value)
        elif choice == '2':
            key = input("Enter key to delete: ")
            ht.delete(key)
        elif choice == '3':
            key = input("Enter key to search: ")
            ht.search(key)
        elif choice == '4':
            ht.display()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
