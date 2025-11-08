# Password Strength Checker

A simple Python script that evaluates the strength of a password based on multiple criteria. It provides a score out of 5 and detailed feedback to help users improve their password security.

## Features

- Checks for:
  - Minimum length (≥ 8 characters)
  - Lowercase letters
  - Uppercase letters
  - Numeric digits
  - Special characters
- Returns:
  - Strength rating: Very Weak, Weak, Moderate, Strong, Very Strong
  - Score out of 5
  - Feedback for each criterion

## How It Works

The script uses regular expressions to analyze the password and assigns points for each satisfied condition. Based on the total score, it categorizes the password strength.

## Usage

1. Clone the repository:
   @bash
   git clone https://github.com/your-username/password-strength-checker.git
   cd password-strength-checker
   

2. Run the script:
   @bash
   python password_checker.py
   

3. Enter a password when prompted. The script will display the strength, score, and feedback.

 #Example Output

Password Strength Checker

Enter password: MyPass123!

Strength: Very Strong
Score: 5/5

  ✓ Good length
  ✓ Has lowercase
  ✓ Has uppercase
  ✓ Has numbers
  ✓ Has special chars

#Requirements

- Python 3.x
- No external dependencies

