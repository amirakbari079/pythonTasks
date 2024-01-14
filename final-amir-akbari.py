print("Menu")
print("1-Add student")
print("2-Enter grades in the system")
print("3-View the student report card")
menu = input("Enter your chose : ")
if menu=="1":
    code = input("Enter student Code : ")
    name = input("Enter student Name : ")
    family = input("Enter student Family : ")
    birth_year = input("Enter student Birth Year : ")
    user_data = code+"-"+name+"-"+family+"-"+birth_year
    with open('data.txt', 'a') as file:
        file.write(user_data+'\n')
elif menu=="2":
    grade_scores = []
    user_exists=False;
    code = input("Enter student Code : ")
    with open('data.txt', 'r') as file:
        for line in file:
            if line.startswith(str(code)):
                user_exists=True
        if user_exists==False :print("There is no user with this code")
    if user_exists:
        for i in range(65, 70):
            grade_score = input(f"Enter student {chr(i)} score: ")
            grade_scores.append(chr(i)+"-"+str(grade_score))
        user_score = code+":"+str(grade_scores)
        with open('score.txt', 'a') as file:
            file.write(user_score+'\n')
elif menu=="3":
    user_exists=False;
    code = input("Enter student Code : ")
    with open('score.txt', 'r') as file:
        for line in file:
            if line.startswith(str(code)):
                print(line.strip())
                user_exists=True
        if user_exists==False :print("There is no user with this code")

