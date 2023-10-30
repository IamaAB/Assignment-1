def factorize(number):
    factors = []
    divisor = 2

    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number = number // divisor
        else:
            divisor += 1

    return factors


number = int(input("Enter a number to factorize: "))
result = factorize(number)
print(f"The factors of {number} are: {result}")
