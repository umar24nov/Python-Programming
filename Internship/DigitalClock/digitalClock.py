import tkinter as tk
from datetime import datetime

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    clock_Label.config(text = current_time)
    clock_Label.after(1000, update_time) # Update every second (1000 milliseconds)
    
    
#  Creating main window
root = tk.Tk()
root.title("Digital Clock")

# Creating a label widget for the clock
clock_Label = tk.Label (root, font = ("Arial", 50), bg = "black", fg = "white")
clock_Label.pack(padx=20,pady=40)

# Initially update time
update_time()

# Start tkinter main loop

root.mainloop()

# Executed Succesfully