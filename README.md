📧 Email Validator (Python)
A simple, logic-based Python script to validate email addresses without using Regular Expressions (Regex). This project demonstrates string manipulation, conditional branching, and loop iteration in Python.

📝 Description
This script asks the user for an email input and verifies if it matches a strict set of custom criteria. It is designed to check for common formatting errors and specific structural rules using nested if-else statements.

✅ Validation Rules
The email is considered valid only if it meets all the following conditions:

Length: The total length must be 6 characters or more.

Start: The first character must be an alphabet (a-z).

@ Symbol: Must contain exactly one @ symbol.

Domain: A dot (.) must be present at either the 3rd or 4th position from the end (e.g., .com or .in).

Format:

No spaces allowed.

No uppercase letters allowed.

No special characters allowed other than @, _, and ..

🚀 How to Run
Prerequisites
Python 3.x installed on your machine.

Steps
Clone the repository:

Bash

git clone https://github.com/yourusername/email-validator.git
Navigate to the directory:

Bash

cd email-validator
Run the script:

Bash

python email_validation.py
Enter an email address when prompted to see the validation result.

🧩 Logic Flow
The script operates using a "Filter" approach. If the input passes the first check, it moves to the second, and so on.

Check Length: Uses len() to ensure minimum size.

Check First Char: Uses .isalpha() on index [0].

Check '@': Uses .count() to ensure uniqueness.

Check Dot Position: Uses bitwise XOR (^) and negative indexing ([-4], [-3]) to ensure the domain extension is valid (2 or 3 characters long).

Character Iteration: Loops through every character to check for white spaces, uppercase letters, or unauthorized special symbols.
