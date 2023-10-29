def binary_to_decimal(number):
    decimal_number = int(number, 2)
    return decimal_number

number = input("Enter a Number : ")
display = binary_to_decimal(number)
print(f"Conversion of {number} to Decimal is :", display)