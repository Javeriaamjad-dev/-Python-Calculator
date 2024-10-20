First_num = int(input("Enter First Number: "))
operator = str(input("Which operation do you want to perform (+, -, *, /): "))
second_num = int(input("Enter Second Number: "))

if operator == '+':
    result = First_num + second_num
elif operator == '-':
    result = First_num - second_num
elif operator == '*':
    result = First_num * second_num
elif operator == '/':
    if second_num != 0:
        result = First_num / second_num
    else:
        result = "Error: Division by zero is not allowed"
else:
    result = "Error: Invalid operator"

print("The result is:", result)


