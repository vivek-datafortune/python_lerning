# Day 1 - Exercise 2: String Operations

print("=== Exercise 2: String Operations ===\n")

email = "john.doe@example.com"

# TODO 1: Extract the username (part before @)
# Hint: use split('@')
username = email.split('@')[0]
name = username.split('.')[0]
print(f"Username: {username}")
print(f"Name: {name}")


# TODO 2: Extract the domain (part after @)
domain  = email.split('@')[1]
print(f"Domain: {domain}")


# TODO 3: Check if the email contains '.com'
has_dot_com = '.com' in email
print(f"Does the email contain '.com'? {isContainsDotCom}")


# TODO 4: Replace '.com' with '.org'
email_org = email.replace('.com', '.org')
print(f"Email with .org: {email_org}")

# TODO 5: Print the email in uppercase
print(f"Email in uppercase: {email.upper()}")

# CHALLENGE: Extract just the domain name without .com
# "john.doe@example.com" -> "example"
domain_name = domain.split('.')[0]
print(f"Domain name without .com: {domain_name}")
