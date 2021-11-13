from tkinter import *

# Create window
window = Tk()

# Customize the window
window.title("Welcome")
window.geometry("720x480")
window.minsize(480, 360)
window.config(background="white")

# Create a frame
frame = Frame(window, bg="white", bd=1, relief=SUNKEN)

# Add a text
lbl_title = Label(frame, text="Welcome to the App", font=("arial", 22, "bold"), bg="white", fg="green", bd=0)
lbl_title.pack()

# Add the frame
frame.pack(expand=YES)

# Print the window
window.mainloop()
