def calculate(num1, num2, operation):
    result = 0
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 != 0:
            result = num1 / num2
        else:
            raise ValueError("Cannot divide by zero")
    print(f"Result: {result}")
    return result


calculate(2, 3, "add") 
# 5

calculate(10, 2, "multiply")
# 20

# to run the file.
# python3 calculator.py