from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    check_mark.config(text="")
    item_label.config(text="Timer")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        count_down(short_break_min)
        item_label.config(text="Short Break", fg=PINK)
    elif reps % 8 == 0:
        count_down(long_break_min)
        item_label.config(text="Long Break", fg=RED)
    else:
        count_down(work_min)
        item_label.config(text="Working Time", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=100, bg=YELLOW)

# Timer Label
item_label = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 15, "bold"), fg=GREEN)
item_label.config(pady=5, padx=20)
item_label.grid(column=1, row=0)

# Tomato Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
# timer text for count_down function
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# start Button
start_button = Button(text="start", command=start_timer)
start_button.grid(column=0, row=2)

# reset Button
reset_button = Button(text="reset", command=reset_timer)
reset_button.grid(column=2, row=2)

# check_mark label
check_mark = Label(bg=YELLOW, font=(FONT_NAME, 10, "bold"), fg=GREEN)
check_mark.config(pady=15)
check_mark.grid(column=1, row=2)

window.mainloop()
