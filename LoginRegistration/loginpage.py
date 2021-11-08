from tkinter import *
from tkinter import messagebox
import pymysql


# ###########################################

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
            cur.execute("SELECT * FROM students WHERE email=%s AND password=%s", (entry_email.get(), entry_password.get()))
            row = cur.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid email or password")
            else:
                messagebox.showinfo("Success", "Welcome")
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
                             activebackground="white", fg="red", activeforeground="red")
btn_forget_password.place(x=410, y=200)

# Login button
btn_login = Button(login_frame, text="Login", font=("arial", 18, "bold"), bg="gray20", bd=0, cursor="hand2",
                   activebackground="gray20", fg="white", activeforeground="white", command=signin)
btn_login.place(x=450, y=240)

entry_email.focus()

window.mainloop()
