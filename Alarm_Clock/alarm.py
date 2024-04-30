import tkinter as tk
import datetime
import time
from pygame import mixer
from tkinter import messagebox


# Initializing the mixer
mixer.init()

# Creating the window
root = tk.Tk()
root.title("Alarm Clock")
root.geometry("550x330")

# variable to manage value of the widget
alarmtime = tk.StringVar()
message = tk.StringVar()

# Label widget
head = tk.Label(root, text="Alarm Clock", font=('comic sans', 20))
head.grid(row=0, columnspan=3, pady=10)

# Alarm functionality
def alarm():
    alarm_t = alarmtime.get()

    def check_time():
        current_time = time.strftime("%H:%M")
        if alarm_t == current_time:
            mixer.music.load("sound.wav")
            mixer.music.play()
            msg = messagebox.showinfo('Info', f'{message.get()}')
            if msg:
                mixer.music.stop()
        else:
            root.after(1000, check_time)  # check again in 1 second

    check_time()

# To display clock Image
clockimg = tk.PhotoImage(file="img_61.png")

# Label widget for image
img = tk.Label(root, image=clockimg)
img.grid(rowspan=5, column=0)

# Label widget for time input
input_time = tk.Label(root, text="Input time", font=('comic sans', 15))
input_time.grid(row=1, column=1)

# Entry widget
altime = tk.Entry(root, textvariable=alarmtime, font=('comic sans', 15), width=6)
altime.grid(row=1, column=2)

# Label widget for message
msg = tk.Label(root, text="Message", font=('comic sans', 15))
msg.grid(row=2, column=1, columnspan=2)

# Entry widget
msg_input = tk.Entry(root, textvariable=message, font=('comic sans', 15))
msg_input.grid(row=3, column=1, columnspan=2)

# Button widget
submit = tk.Button(root, text="Submit", command=alarm, font=('comic sans', 15))
submit.grid(row=4, column=1, columnspan=2)

# Event loop
root.mainloop()
