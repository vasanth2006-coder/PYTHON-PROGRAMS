a = input("Enter a string: ")

result = ""

for ch in a:
    if ch.isupper():
        result = result + ch.lower()
    elif ch.islower():
        result = result + ch.upper()
    else:
        result = result + ch

print("Converted string:", result)
