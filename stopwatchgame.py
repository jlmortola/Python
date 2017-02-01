#"Stopwatch: The Game"
#
# 'Introduction to Interactive Programming in Python' Course
# RICE University
#
# Student: Jose L Mortola
#
# In this game you get a point everytime you stop the watch when
# deci is 0

import simplegui

ticks = 0
count = 0
points = 0
deci = 0
first_click = True

#handler for counting ticks and obtaining mins, secs & deci
def format(ticks):
    global deci, secs
    deci = int((ticks/10)%10)
    secs = int((ticks/100)%60)
    mins = int((ticks/6000)%60)

    if secs < 10:
        return str(mins)+":0"+str(secs)+"."+str(deci)
    else:
        return str(mins)+":"+str(secs)+"."+str(deci)

#handler to start counter
def start():
    global first_click
    first_click = True
    timer.start()

#handler to stop counter
def stop():
    timer.stop()
    global count, first_click, points, deci

    if first_click == True:
        count += 1
        first_click = False
        if deci == 0:
            points += 1

#handler to reset counter
def reset():
    timer.stop()
    global ticks, count, first_click, points
    first_click = False
    ticks = 0
    points = 0
    count = 0

# handler to update and count ticks
def tick():
    global ticks
    ticks +=1

def draw_handler(canvas):
    canvas.draw_text(format(ticks),[70,70],18,"White")
    canvas.draw_text("tries: " + str(count),[40,50],14,"White")
    canvas.draw_text("points: " + str(points),[100,50],14,"White")

frame = simplegui.create_frame("ticker",300,300)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(10,tick)

buttonstart = frame.add_button("start",start)
buttonstop = frame.add_button("stop",stop)
buttonreset = frame.add_button("reset",reset)

frame.start()
