path = "C:/Users/pooja/Desktop/pro_game_development/lesson_11/question_bank.txt"

'''with open(path,"w") as file:
    file.write("What is 30 + 550?, 130, 580, 480, 450, 2")'''

questions = []

with open(path, "r") as file:
    '''ask = file.read()
    print(ask)'''
    for r in file:
        q = r.strip().split(",")
        questions.append(q)
        print(q)

print(questions)

for e in questions:
    print(e[0])
    print(e[1])
    print(e[2])
    print(e[3])
    print(e[4])