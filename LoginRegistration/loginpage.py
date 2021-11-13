from tkinter import *
from tkinter import messagebox, ttk
import pymysql


# ###########################################

def reset_password():
    if entry_email.get() == "":
        messagebox.showerror("Error", "Please fill the email address box to reset your password")
    else:
        try:
            connection = pymysql.connect(host="localhost", user="root", password="3141", database="register")
            cur = connection.cursor()
            cur.execute("SELECT * FROM students WHERE email=%s", (entry_email.get()))
            row = cur.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid email")
            else:
                connection.close()

                # Creating new password function
                def change_password():
                    if entry_security_question.get() == "Select Question" or entry_answer.get() == "" or \
                            entry_new_password.get() == "":
                        messagebox.showerror("Error", "All fields are required")
                    else:
                        try:
                            con = pymysql.connect(host="localhost", user="root", password="3141",
                                                  database="register")
                            cursor = con.cursor()
                            cursor.execute("SELECT * FROM students WHERE email=%s and question=%s and answer=%s",
                                           (entry_email.get(),
                                            entry_security_question.get(), entry_answer.get()))
                            row_data = cur.fetchone()

                            if row_data is None:
                                messagebox.showerror("Error", "Security Question or Answer is incorrect", parent=root)
                            else:
                                cur.execute("UPDATE students set password=%s WHERE email=%s", (entry_new_password.get(),
                                                                                               entry_email.get()))
                                connection.commit()
                                connection.close()
                                messagebox.showinfo("Success", "Password is reset , Please Login to with new password",
                                                    parent=root)
                                entry_security_question.current(0)
                                entry_answer.delete(0, END)
                                entry_new_password.delete(0, END)
                                root.destroy()

                        except Exception as error:
                            messagebox.showerror("Error", f"Error is due to {error}")

                # Creating reset password page
                root = Toplevel()
                root.title("Forget Password")
                root.geometry("470x560+400+60")
                root.config(bg="white")
                root.resizable(False, False)
                root.focus_force()
                root.grab_set()

                # Title Label
                lbl_forget = Label(root, text="Forget", font=("arial", 22, "bold"), bg="white")
                lbl_forget.place(x=120, y=10)
                # Title Label
                lbl_pass = Label(root, text="Password", font=("arial", 22, "bold"), bg="white", fg="green")
                lbl_pass.place(x=225, y=10)

                # Password Image
                password_image = PhotoImage(file="images/pass.png")
                lbl_forget = Label(root, image=password_image, bg="white")
                lbl_forget.place(x=170, y=70)

                # Add Security Question
                lbl_security = Label(root, text="Security Question", font=("times new roman", 18, "bold"),
                                     bg="white")
                lbl_security.place(x=60, y=200)
                # Entry Security Question
                entry_security_question = ttk.Combobox(root, font=("times new roman", 16), state="readonly", width=28)
                entry_security_question["values"] = (
                    "Select Question", "Your First Pet Name?", "Your Birth Place?", "Your Best Friend Name?",
                    "Your Favorite Teacher?",
                    "Your Favorite Hobby?")
                entry_security_question.current(0)
                entry_security_question.place(x=60, y=260)

                # Add Answer Label
                lbl_answer = Label(root, text="Answer", font=("times new roman", 18, "bold"), bg="white")
                lbl_answer.place(x=60, y=310)
                # Entry Answer
                entry_answer = Entry(root, font=("times new roman", 18,), bg="lightgray", width=28)
                entry_answer.place(x=60, y=350)

                # New Password Label
                lbl_new_password = Label(root, text="New Password", font=("times new roman", 18, "bold"), bg="white")
                lbl_new_password.place(x=60, y=400)
                # Entry New Password
                entry_new_password = Entry(root, font=("times new roman", 18,), bg="lightgray", width=28, show="*")
                entry_new_password.place(x=60, y=440)

                # Change password button
                btn_change_password = Button(root, text="Change Password", font=("arial", 14), bg="green", bd=0,
                                             cursor="hand2",
                                             activebackground="green", fg="white", activeforeground="white",
                                             command=change_password)
                btn_change_password.place(x=130, y=500)

                root.mainloop()
        except Exception as e:
            messagebox.showerror("Error", f"Error is due to {e}")


def register_window():
    window.destroy()
    import registration


def signin():
    if entry_email.get() == "" or entry_password.get() == "":
        messagebox.showerror("Error", "All fields are required")
    else:
        try:
            connection = pymysql.connect(host="localhost", user="root", password="3141", database="register")
            cur = connection.cursor()
            cur.execute("SELECT * FROM students WHERE email=%s AND password=%s",
                        (entry_email.get(), entry_password.get()))
            row = cur.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid email or password")
            else:
                messagebox.showinfo("Success", "Welcome")
                window.destroy()
                import welcome
                connection.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error is due to {e}")


# ################GUI###########################
window = Tk()
window.title("Login page")
window.geometry("900x600+50+50")
window.resizable(False, False)

# Add Background
bg = PhotoImage(file="images/loginbg.png")
bg_image = Label(window, image=bg)
bg_image.place(x=0, y=0)

# Login Frame
login_frame = Frame(window, width=560, height=320, bg="white")
login_frame.place(x=180, y=140)

# User Image
user_image = PhotoImage(file="images/user.png")
lbl_user_image = Label(login_frame, image=user_image, bg="white")
lbl_user_image.place(x=10, y=50)

# Email Label
lbl_email = Label(login_frame, text="Email", font=("arial", 22, "bold"), bg="white")
lbl_email.place(x=220, y=32)
# Email Entry
entry_email = Entry(login_frame, font=("arial", 22), bg="lightgray")
entry_email.place(x=220, y=70)

# Password Label
lbl_password = Label(login_frame, text="Password", font=("arial", 22, "bold"), bg="white")
lbl_password.place(x=220, y=120)
# Password Entry
entry_password = Entry(login_frame, font=("arial", 22), bg="lightgray", show="*")
entry_password.place(x=220, y=160)

# Register new account button
btn_register = Button(login_frame, text="Register New Account", font=("arial", 12), bg="white", bd=0, cursor="hand2",
                      activebackground="white", command=register_window)
btn_register.place(x=220, y=200)

# Forget password button
btn_forget_password = Button(login_frame, text="Forget password", font=("arial", 12), bg="white", bd=0, cursor="hand2",
                             activebackground="white", fg="red", activeforeground="red", command=reset_password)
btn_forget_password.place(x=410, y=200)

# Login button
btn_login = Button(login_frame, text="Login", font=("arial", 18, "bold"), bg="gray20", bd=0, cursor="hand2",
                   activebackground="gray20", fg="white", activeforeground="white", command=signin)
btn_login.place(x=450, y=240)

entry_email.focus()

window.mainloop()
