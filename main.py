# PhoneAndEmail.PY (7-15)
# Finds All Phone And Emails In The Text In Clipboard And In The End The Program Copy The Result in Clipboard

# Importing Librarys
import re
import pyperclip
import sys

# Regex Compile
phoneRegex = re.compile(r"09[01239]\d{8}|\+98 ?9[01239]\d ?\d{3} ?\d{2} ?\d{2}")
emailRegex = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

# Paste Result From Clipboard
text = str(pyperclip.paste())

# Find Match
phones = phoneRegex.findall(text)
emails = emailRegex.findall(text)

# Exit if No Matches
if (len(phones)==0)and(len(emails)==0):
    print("No Matches Found.")
    sys.exit()

# Export To User
print("Phones:")
for phone in phones:
    print(phone)
print()
print("Emails:")
for email in emails:
    print(email)

# Copy Result To Clipboard
copy = "\n".join(phones) + "\n\n" + "\n".join(emails)
pyperclip.copy(copy)
print()
print("Copied!")