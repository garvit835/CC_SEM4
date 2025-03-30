from collections import deque

# Function to determine operator precedence
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0

# Function to perform the Shunting Yard Algorithm
def infix_to_postfix(expression):
    output = deque()  # Output queue
    operators = deque()  # Operator stack
    i = 0
    while i < len(expression):
        char = expression[i]

        if char.isalnum():  # If the character is an operand (variable or number)
            # Handle multi-character operands (numbers or variables)
            operand = []
            while i < len(expression) and expression[i].isalnum():
                operand.append(expression[i])
                i += 1
            output.append(''.join(operand))  # Add the complete operand to the output queue
            continue  # Skip the increment of `i` here, since it's done in the inner loop

        elif char == '(':  # If the character is '(', push it to the stack
            operators.append(char)
        
        elif char == ')':  # If the character is ')', pop and output from the stack until '(' is found
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()  # Pop '(' from the stack
        
        else:  # The character is an operator
            while (operators and precedence(operators[-1]) >= precedence(char)):
                output.append(operators.pop())
            operators.append(char)
        
        i += 1  # Increment index

    # Pop all the remaining operators from the stack
    while operators:
        output.append(operators.pop())

    return ''.join(output)

# Read the expression from user input
expression = input("Enter an infix expression: ").strip()

# Convert to postfix notation and print the result
postfix = infix_to_postfix(expression)
print(f"Postfix: {postfix}")
