# from pyinstaller import PyInstaller
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
#25
SHORT_BREAK_MIN = 5
#5
LONG_BREAK_MIN = 20
#20
reps = 0
timers = None


windows = Tk()
windows.title("Pomodoro")
windows.config(padx=100,pady=100,bg=GREEN)

canvas = Canvas(width=200, height=224, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
canvas.config(bg=GREEN)
text_time = canvas.create_text(102, 130,font=(FONT_NAME,38,"bold"),fill="white", text="00:00")
canvas.grid(column=1, row=1)


timer = Label(text="Timer",font=(FONT_NAME,38,"bold"), highlightthickness=0)
timer.grid(column=1, row=0)
timer.config(bg= GREEN)



start = Button(text="Start",font=(FONT_NAME,10,"bold"),fg="blue", highlightthickness=0)
start.grid(column=0, row=2)



def start_timer():
    global reps
    reps += 1
    if reps % 2 == 0:
        if reps == 8:
            timer.config(fg=PINK, text="Break")
            times(LONG_BREAK_MIN*60)
        else:
            timer.config(fg=PINK, text="Break")
            times(SHORT_BREAK_MIN * 60)
    else:
        timer.config(text="Timer", font=(FONT_NAME, 38, "bold"), fg="black")
        times(WORK_MIN*60)


def times(count):
    min = int(count/60)
    sec = int(count%60)

    if sec == 0:
        sec = "00"
        canvas.itemconfig(text_time, text=f"{min}:{sec}")
    elif sec <10:
        canvas.itemconfig(text_time, text=f"{min}:0{sec}")
    else:
        canvas.itemconfig(text_time, text=f"{min}:{sec}")

    if count > 0:
        count -= 1
        global timers
        timers = windows.after(1000, times,count)
    else:
        start_timer()

start.config(bg= GREEN,command=start_timer)


def reset_timer():
    global timers
    windows.after_cancel(timers)
    canvas.itemconfig(text_time, text="00:00")
    timer.config(text="Timer",fg="black")


reset = Button(text="Reset",font=(FONT_NAME,10,"bold"),fg="blue", highlightthickness=0)
reset.grid(column=2, row=2)
reset.config(bg= GREEN, command=reset_timer)


windows.mainloop()

