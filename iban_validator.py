# IBAN Validator.

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')

if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")

    # Lab 2.5.4 - The IBAN Validator
#
# Assumptions:
# 1. The user enters an IBAN containing letters and digits.
# 2. Spaces are allowed in the input and are removed before validation.
# 3. The IBAN must contain only letters and digits after spaces are removed.
# 4. The IBAN must contain at least 15 characters.
# 5. The IBAN must contain no more than 31 characters.
# 6. Letters are converted to uppercase before processing.
# 7. Letters are converted to numbers using:
#       A = 10, B = 11, C = 12, ... Z = 35.
# 8. The IBAN is considered valid if the converted number
#    gives a remainder of 1 when divided by 97.
#
# Tracing:
# Line 01: Ask the user to enter an IBAN.
# Line 02: Remove all spaces from the IBAN.
# Line 04: Check that the IBAN contains only letters and digits.
# Line 05: Display an error if invalid characters are found.
# Line 06: Check whether the IBAN is shorter than 15 characters.
# Line 07: Display an error if it is too short.
# Line 08: Check whether the IBAN is longer than 31 characters.
# Line 09: Display an error if it is too long.
# Line 11: Start processing a correctly formatted IBAN.
# Line 12: Move the first four characters to the end
#          and convert all letters to uppercase.
# Line 13: Create an empty string for the converted IBAN.
# Line 14: Iterate through every character in the IBAN.
# Line 15: Check whether the current character is a digit.
# Line 16: If it is a digit, copy it into iban2.
# Line 17: Otherwise, the character is a letter.
# Line 18: Convert the letter to a number from 10 through 35.
# Line 19: Convert the completed numeric string into an integer.
# Line 20: Divide the number by 97 and check the remainder.
# Line 21: If the remainder is 1, the IBAN is valid.
# Line 23: Otherwise, the IBAN is invalid.
