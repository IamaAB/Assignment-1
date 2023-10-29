cin = int(input("Enter the length of numbers : "))
# taken list
list = []
for i in range(cin):
    list.append(input('Enter a Number: '))

print("Elements in List is : ",list)

maximum = list[0]
minimum = list[0]

for num in list:
    if num> maximum:
        maximum= num
        break
    if num < minimum:
        maximum = num
        break

print("Maximum : ", maximum)
print("Minimum : ", minimum)
