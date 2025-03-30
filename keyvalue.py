class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        """
        A simple hash function: sum of ASCII values of characters in the key,
        modulo the table size.
        """
        return sum(ord(ch) for ch in str(key)) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        # Check if key already exists in the bucket and update it
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                print(f"Updated key '{key}' with value '{value}' at index {index}.")
                return
        # If key doesn't exist, add a new key-value pair
        self.table[index].append((key, value))
        print(f"Inserted key '{key}' with value '{value}' at index {index}.")

    def retrieve(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def display(self):
        print("Hash Table Contents:")
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")

if __name__ == "__main__":
    ht = HashTable()

    while True:
        print("\n--- Hash Table Operations ---")
        print("1. Insert key-value pair")
        print("2. Retrieve value by key")
        print("3. Display hash table")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            key = input("Enter key: ")
            value = input("Enter value: ")
            ht.insert(key, value)
        elif choice == '2':
            key = input("Enter key to retrieve: ")
            result = ht.retrieve(key)
            if result is not None:
                print(f"Value for key '{key}': {result}")
            else:
                print(f"Key '{key}' not found.")
        elif choice == '3':
            ht.display()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")
