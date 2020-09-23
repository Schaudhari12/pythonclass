grade = input("please enter your grade:")
print(f'Your in {grade}th grade, cool!')
if int(grade) <= 5:
    print("You are in elementry")
if int(grade) > 5 and int(grade) <=8:
    print("You are in middle school")
if int(grade) > 8 and int(grade) <=12:
    print("You are in highschool")
