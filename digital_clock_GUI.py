import time
import tkinter as tk

window = tk.Tk()
window.title("Digital Clock")

time_label = tk.Label(window, font=("Helvetica", 48))
time_label.pack(padx=50, pady=20)

def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    window.after(1000, update_time)

update_time()

window.mainloop()
