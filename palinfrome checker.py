# Palindrome Checker

text = input("Enter a word or sentence: ")

# Normalize the input
cleaned_text = text.lower().replace(" ", "")

# Reverse the string
reversed_text = cleaned_text[::-1]

# Check whether it is a palindrome
if cleaned_text == reversed_text:
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")
