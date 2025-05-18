import pgzrun

import random
WIDTH = 870
HEIGHT = 650

TITLE = "Quiz Master"
marquee_message = ""
time_left = 10

marquee_box = Rect(0,0,880,80)
question_box = Rect(0,0,650,150)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)
timer_box = Rect(0,0,150,150)
skip_box = Rect(0,0,150,350)
questions = []
q_count = 0
q_index = 0
question_path = "C:/Users/pooja/Desktop/pro_game_development/lesson_11/question_bank.txt"


marquee_box.move_ip(0,0)
question_box.move_ip(20,50)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
timer_box.move_ip(700,100)
skip_box.move_ip(700,300)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

def draw():
    screen.clear()
    screen.fill(color="yellow")
    screen.draw.filled_rect(marquee_box,"yellow")
    screen.draw.filled_rect(question_box,"blue")
    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box,"blue")
    screen.draw.filled_rect(timer_box,"black")
    screen.draw.filled_rect(skip_box,"purple")
    global marquee_message
    marquee_message = "Welcome to Quiz Master!"
    screen.draw.textbox(marquee_message, marquee_box, color = "black", shadow = (0.5, 0.5), scolor = "white")
    screen.draw.textbox(str(time_left), timer_box, color = "white", shadow = (0.5, 0.5), scolor = "yellow")
    screen.draw.textbox("Skip", skip_box, color = "yellow", shadow = (0.5, 0.5), scolor = "white", angle = 90)
    screen.draw.textbox(q[0], question_box, color = "black", shadow = (0.5, 0.5), scolor = "white")
    index = 1
    for I in answer_boxes:
        screen.draw.textbox(q[index], I, color = "orange")
        index = index+1


def move_text():
    marquee_box.x = marquee_box.x-3
    if marquee_box.right < 0:
        marquee_box.left = WIDTH

def change_time():
    global time_left
    if time_left > 0:
        time_left = time_left-1
    
clock.schedule_interval(change_time, 1)

def update():
    move_text()

def read_questions():
    global questions, q_count
    with open(question_path, "r") as file:
        for r in file:
            questions.append(r)
            q_count = q_count + 1
            

def read_next_question():
    global q_index
    random.shuffle(questions)
    q_index = q_index + 1
    return questions.pop(0).split(",")

def on_mouse_down(pos):
    index=1
    for I in answer_boxes:
        if I.collidepoint(pos):
            if index is int(q[5]):
                correct_answer()
            else:
                game_over()
    if skip_box.collidepoint(pos):
        skip_question()
    
    

read_questions()

random.shuffle(questions)
q = read_next_question()










    


pgzrun.go()