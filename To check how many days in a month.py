n=input("Enter the month:")
if n in ["january","march","may","july","august","october","december"]:
  print("month has 31 days")
elif n in ["april","june","september","november"]:
  print("month has 30 days")
elif n=="february":
  print("february")
else:
  print("invalid month")