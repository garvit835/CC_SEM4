def evaluate_postfix(expression):
    stack = []

    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            val2 = stack.pop()
            val1 = stack.pop()

            if token == '+':
                stack.append(val1 + val2)
            elif token == '-':
                stack.append(val1 - val2)
            elif token == '*':
                stack.append(val1 * val2)
            elif token == '/':
                stack.append(val1 / val2)
            else:
                print("Unknown operator:", token)
                return None

    return stack.pop()

# Example usage
expr = "5 1 2 + 4 * + 3 -"
result = evaluate_postfix(expr)
print("Result:", result)
