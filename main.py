password = input("Enter your password: ")

length = len(password)
has_uppercase = any(char.isupper() for char in password)

print("Password length:", length)
print("Contains uppercase:", has_uppercase)
