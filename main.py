password = input("Enter your password: ")

length = len(password)
has_uppercase = any(char.isupper() for char in password)
has_lowercase = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

print("Password length:", length)
print("Contains uppercase:", has_uppercase)
print("Contains lowercase:", has_lowercase)
print("Contains digit:", has_digit)
print("Contains special character:", has_special)
