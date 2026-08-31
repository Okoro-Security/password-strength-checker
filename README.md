# Password Strength Checker

A simple Python tool that analyzes password strength based on common security criteria.

## Features

- Checks password length
- Detects uppercase letters
- Detects lowercase letters
- Detects numbers
- Detects special characters
- Calculates a security score
- Classifies the password as Weak, Medium, or Strong
- Provides suggestions to improve weak passwords
- Hides password input for better privacy

## Technologies

- Python 3
- Git
- GitHub

## How It Works

The program evaluates a password using five criteria:

1. Minimum length of 8 characters
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one number
5. At least one special character

Each satisfied criterion contributes one point to the final score.

## Example

```text
Enter your password:

--- Password Analysis ---
Length: 11
Uppercase: True
Lowercase: True
Digit: True
Special character: True
Score: 5 / 5
Strength: Strong

Your password meets all security criteria.
