from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


class Login:
    def __init__(self, window):
        self.window = window
        self.window.title("Login System")
        self.window.geometry("1199x600+150+100")
        self.window.resizable(False, False)

        # Add background
        self.bg = ImageTk.PhotoImage(file="images/bg.jpg")
        self.bg_image = Label(self.window, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Login Frame
        login_frame = Frame(self.window, bg="white")
        login_frame.place(x=300, y=150, width=500, height=400)

        # Add Title
        lbl_title = Label(login_frame, text="Login Here", font=("Impact", 35, "bold"), fg="#6162FF",
                          bg="white").place(x=90, y=30)

        # Add Sub title
        lbl_subtitle = Label(login_frame, text="Memmbers Login Area", font=("Goudy old style", 15, "bold"),
                             fg="#1d1d1d", bg="white").place(x=90, y=100)

        # Add Username Label
        lbl_username = Label(login_frame, text="Username", font=("Goudy old style", 15, "bold"),
                             fg="grey", bg="white").place(x=90, y=140)

        # Username Text Entry
        self.txt_username = Entry(login_frame, font=("Goudy old style", 15),
                                  bg="#E7E6E6")
        self.txt_username.place(x=90, y=170, width=320, height=35)

        # Add Password Label
        lbl_password = Label(login_frame, text="Password", font=("Goudy old style", 15, "bold"),
                             fg="grey", bg="white").place(x=90, y=220)

        # Password Text Entry
        self.txt_password = Entry(login_frame, font=("Goudy old style", 15, "bold"),
                                  bg="#E7E6E6")
        self.txt_password.place(x=90, y=250, width=320, height=35)

        # Forget Button
        btn_forget = Button(login_frame, text="Forget Password?", font=("Goudy old style", 12),
                            fg="#6162FF", bg="white", bd=0, cursor="hand2").place(x=290, y=290)

        # Login Button
        btn_login = Button(login_frame, text="Login", font=("Goudy old style", 12),
                           fg="white", bg="#6162FF", bd=0, command=self.check, cursor="hand2").place(x=90, y=320,
                                                                                                     width=180,
                                                                                                     height=40)

    def check(self):
        if self.txt_username.get() == "" or self.txt_password == "":
            messagebox.showerror("Error", "All fields are required", parent=self.window)
        elif self.txt_username.get() != "admin" or self.txt_password != "1234":
            messagebox.showerror("Error", "Invalid Username or password", parent=self.window)
        else:
            messagebox.showinfo("Welcome", f"Welcome {self.txt_username.get()}")


window = Tk()
login = Login(window)
window.mainloop()
