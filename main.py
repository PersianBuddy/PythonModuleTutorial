import re

# extract email from a text using regular expressions
sample_text = "This a sample text, mnajafi0014@gmail.comsdfw I want to extract this email from it"

email_pattern = re.compile("[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+.[com|net|org]")

extracted_email = email_pattern.search(sample_text)
print(extracted_email)

