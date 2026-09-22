import re

def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    if score <= 2:
        return "Weak"
    elif score in (3, 4):
        return "Moderate"
    else:
        return "Strong"

password = input("Enter a password to check: ")
result = check_strength(password)
print("Password strength:", result)
