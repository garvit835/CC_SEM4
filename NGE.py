def next_greater_element(arr):
    stack = []
    nge = [-1] * len(arr)
    
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            index = stack.pop()
            nge[index] = arr[i]
        stack.append(i)
    
    return nge

# Input from the user
arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
result = next_greater_element(arr)

print("Next Greater Elements:", result)
