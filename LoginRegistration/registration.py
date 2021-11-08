from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql


# Create the login window
def login_window():
    window.destroy()
    import loginpage


# Clear Function
def clear():
    entry_firstname.delete(0, END)
    entry_lastname.delete(0, END)
    entry_contact.delete(0, END)
    entry_email.delete(0, END)
    entry_security_question.current(0)
    entry_answer.delete(0, END)
    entry_password.delete(0, END)
    entry_confirm_password.delete(0, END)
    check.set(0)
    entry_firstname.focus()


# Register Function
def register():
    if entry_firstname.get() == "" or entry_lastname.get() == "" or entry_email.get() == "" or \
            entry_contact.get() == "" or entry_password.get() == "" or entry_confirm_password.get() == "" or \
            entry_security_question.get() == "Select Question" or entry_answer.get() == "":
        messagebox.showerror("Error", "All fields are required")

    elif entry_password.get() != entry_confirm_password.get():
        messagebox.showerror("Error", "Password Mismatch")
    elif check.get() == 0:
        messagebox.showerror("Error", "Please agree to our terms & conditions")
    else:
        try:
            connection = pymysql.connect(host="localhost", user="root", password="3141", database="register")
            cur = connection.cursor()
            cur.execute("SELECT * FROM students WHERE email=%s", entry_email.get())
            row = cur.fetchone()

            if row != None:
                messagebox.showerror("Error", "User already exists")
            else:
                cur.execute(
                    "Insert INTO students (f_name,l_name,contact,email,question,answer,password) VALUES(%s,%s,%s,"
                    "%s,%s,%s,%s)", (entry_firstname.get(), entry_lastname.get(), entry_contact.get(),
                                     entry_email.get(), entry_security_question.get(),
                                     entry_answer.get(), entry_password.get()))
                connection.commit()
                connection.close()

                messagebox.showinfo("Success", "Registration is successful")

                clear()

                login_window()

        except Exception as e:
            messagebox.showerror("Error", f"Error due to {e}")


window = Tk()
window.title("Registration Page")
window.geometry("1350x710+100+50")
window.resizable(False, False)

# Add Background
bg = PhotoImage(file="images/bg.png")
bg_image = Label(window, image=bg)
bg_image.place(x=0, y=0)

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
lbl_contact = Label(register_frame, text="Phone Number", font=("times new roman", 18, "bold"), fg="gray20")
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
entry_security_question = ttk.Combobox(register_frame, font=("times new roman", 16), state="readonly")
entry_security_question["values"] = (
    "Select Question", "Your First Pet Name?", "Your Birth Place?", "Your Best Friend Name?",
    "Your Favorite Teacher?",
    "Your Favorite Hobby?")
entry_security_question.current(0)
entry_security_question.place(x=20, y=355)

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
entry_password = Entry(register_frame, font=("times new roman", 18,), bg="lightgray", show="*")
entry_password.place(x=20, y=475)

# Add Confirm Password Label
lbl_confirm_password = Label(register_frame, text="Confirm Password", font=("times new roman", 18, "bold"),
                             fg="gray20")
lbl_confirm_password.place(x=370, y=440)
# Entry Confirm password
entry_confirm_password = Entry(register_frame, font=("times new roman", 18,), bg="lightgray", show="*")
entry_confirm_password.place(x=370, y=475)

# Add Check Button
check = IntVar()
btn_check = Checkbutton(register_frame, text="I Agree All The Terms & Conditions",
                        font=("times new roman", 14, "bold"), onvalue=1, offvalue=0, variable=check)
btn_check.place(x=20, y=530)

# Add Register Button
register_image = PhotoImage(file="images/register.png")
btn_register = Button(register_frame, image=register_image, bd=0, cursor="hand2", command=register)
btn_register.place(x=250, y=580)

# Add Login Button
login_image = PhotoImage(file="images/login.png")
btn_login = Button(window, image=login_image, bd=0, cursor="hand2", bg="gold", command=login_window)
btn_login.place(x=240, y=330)

entry_firstname.focus()
window.mainloop()
