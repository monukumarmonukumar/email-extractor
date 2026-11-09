
import re

# Read the input text file
with open("emails.txt", "r") as file:
    text = file.read()

# Find all email addresses
emails = re.findall(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    text
)

# Remove duplicate emails
unique_emails = sorted(set(emails))

# Save emails into a new file
with open("extracted_emails.txt", "w") as file:
    for email in unique_emails:
        file.write(email + "\n")

print("Email extraction completed successfully!")
print("Total unique emails found:", len(unique_emails))
print("Saved in extracted_emails.txt")
