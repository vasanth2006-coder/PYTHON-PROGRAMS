a=input(" enter string:")
b=a.split()
unique_words=[]
for word in b:
    if word not in unique_words:
        unique_words.append(word)
result=" ".join(unique_words)
print("original string:",a)
print(" after removing duplicates:",result)

















