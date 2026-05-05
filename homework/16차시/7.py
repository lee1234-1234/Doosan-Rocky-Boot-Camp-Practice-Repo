def calc_postfix(e):
    stack = []
    tokens = e.split()
    
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            
            if token == "+":
                result = num1 + num2
            elif token == "-":
                result = num1 - num2
            elif token == "*":
                result = num1 * num2
            elif token == "/":
                result = num1 / num2
            
            stack.append(result)
    return stack.pop()
    
print(calc_postfix("3 4 +"))