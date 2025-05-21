import re  # Regular expressions to search patterns

# Function to check password strength
def check_password_strength(password):
    score = 0

    # Block common passwords
    common_passwords = ['password123', '12345678', 'qwerty', 'letmein']
    if password.lower() in common_passwords:
        print("❌ This password is too common. Choose something unique.")
        return

    # Rule 1: Minimum length
    if len(password) >= 8:
        score += 1
    else:
        print("❌ Password should be at least 8 characters long.")

    # Rule 2: Uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        print("❌ Include both uppercase and lowercase letters.")

    # Rule 3: At least one digit
    if re.search(r"\d", password):
        score += 1
    else:
        print("❌ Add at least one number (0-9).")

    # Rule 4: At least one special character
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        print("❌ Include at least one special character (!@#$%^&*).")

    # Full score if all 4 rules are satisfied
    if score == 4:
        score += 1

    # Result
    print("\n🔐 Password Strength Score:", score, "/ 5")

    if score == 5:
        print("✅ Strong Password! Great job!")
    elif score >= 3:
        print("⚠️ Moderate Password - Consider making it stronger.")
    else:
        print("❌ Weak Password - Improve it using the suggestions above.")

# Get password from user
user_password = input("Enter your password: ")
check_password_strength(user_password)
