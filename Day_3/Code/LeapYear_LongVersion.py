# 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

divisible2 = 4
divisible3 = 100
divisible4 = 400
year = int(input("Which year do you want to check? "))

# initializing the variable 
mod4check = 0
mod100check = 0
mod400check = 0

# 0 = False
# 1 = True 

if year % divisible2 == 0:
   print("divisible by 4")
   mod4check = 1
else: 
   print("not divisible by 4")
   mod4check = 0


if year % divisible3 == 0:
   print("divisible by 100")
   mod100check = 1
else: 
   print("not divisible by 100")
   mod100check = 0


if year % divisible4 == 0:
   print("divisible by 400")
   mod400check = 1
else: 
   print("not divisible by 400")
   mod400check = 0


 # mod4check and not mod100check and not mod400check: divisible by 4 but not by 100 or 400
 # mod4check and not mod100check and mod400check: divisible by 4 and 400 but not 100
 # mod4check and mod100check and mod400check: divisible by 4, 100, and 400

if mod4check and not mod100check and not mod400check:
    print("This year is a leap year. ")
elif mod4check and not mod100check and mod400check:
    print("This year is a leap year. ")
elif mod4check and mod100check and mod400check:
    print("This year is a leap year. ")
else:
    print("This is not a leap year. ")





