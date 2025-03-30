import heapq

def get_input():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    return nums

def product_of_top_three_distinct(nums):
    distinct_nums = list(set(nums))

    if len(distinct_nums) < 3:
        print("Not enough distinct elements.")
        return

    # Use max heap by inverting values
    max_heap = [-num for num in distinct_nums]
    heapq.heapify(max_heap)

    first = -heapq.heappop(max_heap)
    second = -heapq.heappop(max_heap)
    third = -heapq.heappop(max_heap)

    product = first * second * third

    print(f"Top 3 largest distinct elements: {first}, {second}, {third}")
    print(f"Product: {product}")

# Menu-Driven Interaction
if __name__ == "__main__":
    nums = []

    while True:
        print("\n--- Product of Top 3 Distinct Elements ---")
        print("1. Enter numbers")
        print("2. Find product of 3 largest distinct elements")
        print("3. Show current list")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            nums = get_input()
        elif choice == '2':
            if not nums:
                print("Please enter numbers first.")
            else:
                product_of_top_three_distinct(nums)
        elif choice == '3':
            print("Current list:", nums)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")
