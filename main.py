def check_password(password):
    length = len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    score = 0

    if length >= 8:
        score += 1

    if has_uppercase:
        score += 1

    if has_lowercase:
        score += 1

    if has_digit:
        score += 1

    if has_special:
        score += 1

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return score, strength


password = input("Enter your password: ")

score, strength = check_password(password)

print("Password score:", score, "/ 5")
print("Password strength:", strength)

if strength == "Weak":
    print("⚠️ Your password is too weak.")
elif strength == "Medium":
    print("⚠️ Your password could be stronger.")
else:
    print("✅ Your password is strong.")

print("Thank you for using Password Strength Checker!")
