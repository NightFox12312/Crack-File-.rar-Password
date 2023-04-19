# RAR Password Cracker

This is a Python script that attempts to crack the password of a RAR file using a brute force approach. It generates combinations of keyboard characters of a specified length and tests them as passwords to unlock the RAR file.

# Requirements

- rarfile Python library: You can install it using pip install rarfile

# Usage

1. Set the desired password length by changing the value of a variable in the script.
2. Specify the path of the RAR file you want to crack by updating the rar_file variable in the script.
3. Run the script using a Python interpreter.
4. The script will iterate through all possible combinations of keyboard characters of the specified length and test them as passwords to unlock the RAR file.
5. If a correct password is found, it will be printed as "Success! Password found: {password}" and the script will terminate.
6. If the password is not found after trying all combinations, it will print "Password not found.".

Note: Please ensure that you have the legal rights and permissions to crack passwords for the RAR file you are attempting to unlock. Unauthorized use of this script may violate laws and regulations.
