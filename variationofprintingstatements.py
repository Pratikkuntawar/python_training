import math_utils
# simple hello world Statements
print("Hello, World!!")

# learning aabout printing variables in python
Name="Pratik"
LastName="Kuntawar"
College="SSGMCE"
Age=23
print(f"My Name is {Name}")
print("Hello,My Name is",Name," ",LastName,"and in last month i am graduated from",College," currently i am ",Age,"years old")

# learn about how can we make use of seprators 
dob = "-".join(["14", "10", "2002"])
print("Hello,My Name is",Name," ",LastName,"and in last month i am graduated from",College," currently i am ",Age,"years old and my date of birth is",dob)

name=input("Enter Your Name here:")
print(type(name))
print(f"Your Entered Name is {name}")

# we can also take integer as an input
age=int(input("Enter Your Age:"))
print(type(age))
print(f"My age is {age}")

print(f"sum of 10 and 5 is {math_utils.add(10,5)}")
print(f"The area of circle having radius 7 is {2*math_utils.PI*7}")