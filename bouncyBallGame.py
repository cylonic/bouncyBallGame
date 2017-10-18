#W
#CS101
#Lab 6

#This program is a small game, the goal is to click the bouncing ball.
#The ball moves quicker as you click it, and the timer is always counting down
#if the timer reaches 0, game over. Clicking the ball awards extra time




from tkinter import *
from random import randrange
from tkinter import ttk
import time

root = Tk()
root.title('Catch me          if you can')



def Score():
    #keep track of player score
    value = score.get()
    return int(value+1)

def callback(event):
    #what happens when the ball is clicked
    global deltax, deltay, score, sec
    x1, y1, x2, y2 = frame.bbox('ball') #coordinates of the ball widget
    if x1 <= event.x <= x2 and y1 <= event.y <= y2:
        #changing speeds and direction of ball
        if deltax < 0:
            deltax -= 1
        if deltax > 0:
            deltax += 1
        if deltay < 0:
            deltay -= 1
        if deltay > 0:
            deltay += 1
        score += 1
        sec += 1
        s.set(score)


#variables
score = 0
sec = 15
total_time = 0
timer = StringVar()
s = StringVar()
deltax = 2
deltay = 2

#setup of window
frame = Canvas(root, width = 700, height = 600)
scoreFrame = Canvas(frame, width = 350, height = 100)
scoreFrame.place(in_=frame, anchor = 'sw', relx=0, rely=1)
timeFrame = Canvas(frame, width = 350, height = 100)
timeFrame.place(in_=frame, anchor = 'se', relx = .5, rely = 1)

#extra frame for socre and timer
w = LabelFrame(scoreFrame, text = 'Score: ')
w.pack(fill = "both", expand = "yes")
l = Label(w, textvariable = s)
l.pack()

t = LabelFrame(timeFrame, text = 'Time: ')
t.pack(fill = "both", expand = "yes")
timeLabel = Label(t, textvariable = timer)
timeLabel.pack()

#event for mouse click
frame.bind("<Button-1>", callback)
frame.pack()
frame.create_rectangle(5, 5, 699, 499)
frame.create_oval(200, 150, 250, 200, fill = 'red', tag = 'ball')
#frame.bind("<Button-1>", callback) # I had 2 of these? Still worked..uncomment if something goofy happens


while True:
    for i in range(1001):
        if i == 1000: #never leave for loop
            i = 1
        if i % 100 == 0: #creating small amount of randomness to ball movement
            deltax = -randrange(deltax-2, deltax + 2)
            deltay = -randrange(deltay-2, deltay + 2)
        if i % 50 == 0: #handling the time
            sec -= 1
            total_time += 1
            timer.set(sec)
        if sec <= 0: #game over
            top = Toplevel()
            top.title('GAME OVER')

            #game over pop up message
            msg = Message(top, text = 'You lost')
            msg2 = Message(top, text = 'Score: ' + str(score))
            msg3 = Message(top, text = 'You lasted ' + str(total_time) + ' seconds!')
            button = Button(top, text = '  Better luck next time   ', command = top.destroy)
            msg.pack()
            msg2.pack()
            msg3.pack(fill = BOTH, expand = 1)
            button.pack()

            #game over message also printed to shell
            print("You lose!")
            print("You scored ", score)
            print("You lasted ", total_time, " seconds!")
            sys.exit()
            

        #ensure ball doesnt go out of bounds
        x1, y1, x2, y2 = frame.bbox('ball')
        if x1 > 650:
            deltax = -deltax
        if x2 < 50:
            deltax = -deltax
        if y1 > 450:
            deltay = -deltay
        if y2 < 50:
            deltay = -deltay

        #handling ball movement
        newDx = deltax
        newDy = deltay
        frame.move('ball', newDx, newDy)
        frame.update()
        frame.after(20)

    
    



root.mainloop()

