import  pgzrun

WIDTH = 900
HEIGHT = 600
TITLE = "Easter Card"

title_box  = Rect(0,0,850,40)
message_box = Rect(0,0,750,300)

title_box.move_ip(25,25)
message_box.move_ip(75,100)

#message_box.move_ip()

def draw():
    screen.clear()
    screen.fill(color="green")
    screen.draw.filled_rect(title_box,"red")
    screen.draw.filled_rect(message_box,"blue")
    global title_message
    title_message = "HAPPY EASTER!"
    screen.draw.textbox(title_message, title_box, color = "navy blue", shadow = (0.5, 0.5), scolor = "green")
    screen.draw.textbox("I hope you had a lovely Easter! How many Easter Eggs did you collect?",  message_box, color = "yellow", shadow =  (0.5, 0.5), scolor = "black")

def move_title():
    title_box.x = title_box.x-3
    if title_box.right < 0:
        title_box.left = WIDTH

def update():
    move_title()


    
    














pgzrun.go()