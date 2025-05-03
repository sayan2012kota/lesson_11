import pgzrun

WIDTH = 900
HEIGHT = 600

TITLE = "Mother's Day card"

message_box = Rect(0,0,850,300)

message_box.move_ip(25,125)

def draw():
    screen.clear()
    screen.fill(color="green")
    screen.draw.filled_rect(message_box,"blue")
    screen.draw.textbox("Happy Mother's day mum!            How was your day? I hope you had a lot of fun on mother's day.        From, Sayan        xxx" ,  message_box)



pgzrun.go()
