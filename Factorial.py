def factorial(input):
    if input == 1:
        return input
    elif input == 0 or input < 0:
        return (" Enter a number greater than 0")
    else:
        output = input*factorial(input-1)
        return output


cin = int(input("Enter a number : "))
display = factorial(cin)
print(f"Factorial of {cin} is : ",display)