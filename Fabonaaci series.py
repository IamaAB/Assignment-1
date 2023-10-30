first_value = 0
second_value = 1
count = 0

while count < 10:
    last_value = first_value + second_value
    if last_value >= 100:
        break  # Break the loop if the next Fibonacci number is 100 or greater
    print(last_value)
    first_value = second_value
    second_value = last_value
    count += 1
