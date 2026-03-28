name=input("enter student name:")
m1=int(input("enter marks of subject 1:"))
m2=int(input("enter marks of subject 2:"))
m3=int(input("enter marks of subject 3:"))
total=m1+m2+m3
percentage=total/3
print("\n---result---")
print("name:",name)
print("total marks:",total)
print("percentage:",percentage)
if percentage>=90:
  print("grade: A")
elif percentage>=75:
  print("grade: B")
elif percentage>=50:
  print("grade: C")
else:
  print("grade: Fail")
if percentage<50:
  print("needs improvement.")
elif percentage<75:
  print("can do better.")
else:
  print("excellent performance!")
