import secrets
import string

char = string.ascii_letters + string.digits

password_length = int(input("Enter Length of Password: "))

# random password
random_password = ''.join(secrets.choice(char)

for _ in range(password_length))

print(f"Random Password of length {password_length} is : ",random_password)
