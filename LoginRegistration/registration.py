from tkinter import *
from tkinter import ttk
from PIL import ImageTk


class RegistrationForm:

    def __init__(self, root):
        self.window = root
        self.window.title("Registration Form")
        self.window.geometry("1350x710+100+50")
        self.window.resizable(False, False)

        # Add Background
        self.bg = PhotoImage(file="images/bg.png")
        self.bg_image = Label(self.window, image=self.bg)
        self.bg_image.place(x=0, y=0)

        # Add Frame
        register_frame = Frame(window, width=650, height=650)
        register_frame.place(x=630, y=30)

        # Add Registration Title Label
        lbl_title = Label(register_frame, text="Registration Form", font=("arial", 22, "bold"), fg="gold")
        lbl_title.place(x=20, y=30)
        # Add First Name Label
        lbl_firstname = Label(register_frame, text="First Name", font=("times new roman", 18, "bold"), fg="gray20")
        lbl_firstname.place(x=20, y=80)

        # Entry First Name
        entry_firstname = Entry(register_frame, font=("times new roman", 18,), bg="lightgray")
        entry_firstname.place(x=20, y=115)

        # Add Last Name Label
        lbl_lastname = Label(register_frame, text="Last Name", font=("times new roman", 18, "bold"), fg="gray20")
        lbl_lastname.place(x=370, y=80)
        # Entry Last Name
        entry_lastname = Entry(register_frame, font=("times new roman", 18,), bg="lightgray")
        entry_lastname.place(x=370, y=115)

        # Add Contact Number Label
        lbl_contact = Label(register_frame, text="Contact", font=("times new roman", 18, "bold"), fg="gray20")
        lbl_contact.place(x=20, y=200)
        # Entry Contact Number
        entry_contact = Entry(register_frame, font=("times new roman", 18,), bg="lightgray")
        entry_contact.place(x=20, y=235)

        # Add Email Label
        lbl_email = Label(register_frame, text="Email", font=("times new roman", 18, "bold"), fg="gray20")
        lbl_email.place(x=370, y=200)
        # Entry Email
        entry_email = Entry(register_frame, font=("times new roman", 18,), bg="lightgray")
        entry_email.place(x=370, y=235)

        # Add Security Question
        lbl_security = Label(register_frame, text="Security Question", font=("times new roman", 18, "bold"),
                             fg="gray20")
        lbl_security.place(x=20, y=320)
        # Entry Security Question
        entry_security = ttk.Combobox(register_frame, font=("times new roman", 16), state="readonly")
        entry_security["values"] = (
            "Select Questions", "Your First Pet Name?", "Your Birth Place?", "Your Best Friend Name?",
            "Your Favorite Teacher?",
            "Your Favorite Hobby?")
        entry_security.current(0)
        entry_security.place(x=20, y=355)

        # Add Answer Label
        lbl_answer = Label(register_frame, text="Answer", font=("times new roman", 18, "bold"), fg="gray20")
        lbl_answer.place(x=370, y=320)
        # Entry Email
        entry_answer = Entry(register_frame, font=("times new roman", 18,), bg="lightgray")
        entry_answer.place(x=370, y=355)

        # Add Password Label
        lbl_password = Label(register_frame, text="Password", font=("times new roman", 18, "bold"), fg="gray20")
        lbl_password.place(x=20, y=440)
        # Entry password
        entry_password = Entry(register_frame, font=("times new roman", 18,), bg="lightgray")
        entry_password.place(x=20, y=475)

        # Add Confirm Password Label
        lbl_confirm_password = Label(register_frame, text="Confirm Password", font=("times new roman", 18, "bold"),
                                     fg="gray20")
        lbl_confirm_password.place(x=370, y=440)
        # Entry Confirm password
        entry_confirm_password = Entry(register_frame, font=("times new roman", 18,), bg="lightgray")
        entry_confirm_password.place(x=370, y=475)

        # Add Check Button
        btn_check = Checkbutton(register_frame, text="I Agree All The Terms & Conditions",
                                font=("times new roman", 14, "bold"), onvalue=1, offvalue=0)
        btn_check.place(x=20, y=530)

        # Add Register Button
        btn_register = Button(register_frame, text="Register Now", font=("times new roman", 18, "bold"),
                              fg="white", bg="gold", bd=0, cursor="hand2", width=15)
        btn_register.place(x=250, y=580)

        # Add Login Button
        btn_login = Button(window, text="Login Now", font=("times new roman", 18, "bold"),
                              fg="white", bg="gold", bd=0, cursor="hand2", width=15)
        btn_login.place(x=240, y=330)


window = Tk()
registration = RegistrationForm(window)
window.mainloop()
