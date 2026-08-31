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

    if length < 8:
        strength = "Weak"
    elif score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return {
        "length": length,
        "uppercase": has_uppercase,
        "lowercase": has_lowercase,
        "digit": has_digit,
        "special": has_special,
        "score": score,
        "strength": strength
    }


password = input("Enter your password: ")

result = check_password(password)

print("\n--- Password Analysis ---")
print("Length:", result["length"])
print("Uppercase:", result["uppercase"])
print("Lowercase:", result["lowercase"])
print("Digit:", result["digit"])
print("Special character:", result["special"])
print("Score:", result["score"], "/ 5")
print("Strength:", result["strength"])

if result["strength"] == "Weak":
    print("⚠️ Your password is too weak.")
elif result["strength"] == "Medium":
    print("⚠️ Your password could be stronger.")
else:
    print("✅ Your password is strong.")

print("\nThank you for using Password Strength Checker!")
