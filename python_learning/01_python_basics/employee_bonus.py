Name = input("Enter Employee name: ")
Experience = int(input("Enter your experience: "))
Current_CTC = int(input("Enter your present CTC: "))

if Experience >= 15:
    bonus = 20 # bonus 20%
    new_CTC = Current_CTC + (Current_CTC*0.2)
else:
    bonus = 10 # bonus 10%
    new_CTC = Current_CTC + (Current_CTC*0.1)

print("Employee name: ", Name)
print("Experience: ", Experience)
print("Present CTC: ", Current_CTC)
print("New CTC: ", new_CTC)