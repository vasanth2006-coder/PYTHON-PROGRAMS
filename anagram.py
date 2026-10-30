a = input("Enter first string: ")
b = input("Enter second string: ")
c = a.lower()
d = b.lower()
if sorted(c) == sorted(d):
    print("Anagram")
else:
    print("Not anagram")
