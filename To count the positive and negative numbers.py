numbers=[-3,-2,-1,0,1,2,3]
positive=0
negative=0
for num in numbers:
  if num>0:
    positive+=1
  elif num<0:
    negative+=1
print("positive numbers:",positive)
print("negative numbers:",negative)
