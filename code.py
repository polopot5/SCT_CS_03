import re

def check_password(password):
    """Assess password strength and return score with feedback."""
    score = 0
    feedback = []
    
    
    if len(password) >= 8:
        score += 1
        feedback.append("✓ Good length")
    else:
        feedback.append("❌ Too short (min 8 chars)")
    

    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("✓ Has lowercase")
    else:
        feedback.append("❌ Missing lowercase")
    
    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("✓ Has uppercase")
    else:
        feedback.append("❌ Missing uppercase")
    
    if re.search(r'\d', password):
        score += 1
        feedback.append("✓ Has numbers")
    else:
        feedback.append("❌ Missing numbers")
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>_\-+=]', password):
        score += 1
        feedback.append("✓ Has special chars")
    else:
        feedback.append("❌ Missing special chars")
    
    
    if score < 2:
        strength = "Very Weak"
    elif score < 3:
        strength = "Weak"
    elif score < 4:
        strength = "Moderate"
    elif score < 5:
        strength = "Strong"
    else:
        strength = "Very Strong"
    
    return strength, score, feedback

print("Password Strength Checker\n")
password = input("Enter password: ")

strength, score, feedback = check_password(password)

print(f"\nStrength: {strength}")
print(f"Score: {score}/5\n")
for item in feedback:
    print(f"  {item}")