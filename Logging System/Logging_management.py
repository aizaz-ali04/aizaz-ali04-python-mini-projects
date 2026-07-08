import tkinter as tk
import json

window = tk.Tk()
window.title("User Manager")
window.geometry("700x500")

# PAGE CHANGE FUNCTIONS

def open_page2():
    page1.pack_forget()
    page2.pack(fill="both", expand=True)
    show_data()


def back_page():
    page2.pack_forget()
    page1.pack(fill="both", expand=True)


# SAVE USER

def login():

    try:
        name = entry_name.get()
        username = entry_username.get()
        email = entry_email.get()

        data = {
            "name": name,
            "username": username,
            "email": email
        }

        # READ FILE
        try:
            with open("users.json", "r") as f:
                users = json.load(f)

        except:
            users = []

        # ADD USER
        users.append(data)

        # SAVE FILE
        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)

        result_label.config(text="User Saved!")

        # CLEAR INPUTS
        entry_name.delete(0, tk.END)
        entry_username.delete(0, tk.END)
        entry_email.delete(0, tk.END)

    except Exception as e:
        result_label.config(text="Error Saving User")
        print(e)


# SHOW USERS

def show_data():

    # CLEAR OLD DATA
    for widget in display_frame.winfo_children():
        widget.destroy()

    try:
        with open("users.json", "r") as f:
            users = json.load(f)

        for user in users:

            row = tk.Frame(display_frame)
            row.pack(fill="x", pady=5)

            info = (
                f"Name: {user['name']} | "
                f"Username: {user['username']} | "
                f"Email: {user['email']}"
            )

            tk.Label(row,text=info,anchor="w").pack(side="left")

            # DELETE BUTTON
            tk.Button(row,text="Delete",command=lambda u=user["username"]: delete_user(u)).pack(side="right")

    except:
        tk.Label(display_frame, text="No Data Found").pack()

# UPDATE USER             

def update_user():

    try:
        username = entry_username.get()
        new_name = entry_name.get()
        new_email = entry_email.get()

        with open("users.json", "r") as f:
            users = json.load(f)

        found = False

        for user in users:

            if user["username"] == username:

                user["name"] = new_name
                user["email"] = new_email

                found = True

        if found:

            with open("users.json", "w") as f:
                json.dump(users, f, indent=4)

            result_label.config(text="User Updated!")

        else:
            result_label.config(text="User Not Found!")

    except Exception as e:
        result_label.config(text="Error Updating User")
        print(e)


# DELETE USER

def delete_user(username):

    try:
        with open("users.json", "r") as f:
            users = json.load(f)

        users = [
            user for user in users
            if user["username"] != username
        ]

        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)

        show_data()

    except Exception as e:
        print(e)


# PAGE 1

page1 = tk.Frame(window)

tk.Label(page1,text="USER FORM",font=("Arial", 18)).pack(pady=10)


# NAME
tk.Label(page1, text="Enter Name").pack()

entry_name = tk.Entry(page1, width=40)
entry_name.pack()


# USERNAME
tk.Label(page1, text="Enter Username").pack()

entry_username = tk.Entry(page1, width=40)
entry_username.pack()


# EMAIL
tk.Label(page1, text="Enter Email").pack()

entry_email = tk.Entry(page1, width=40)
entry_email.pack()


# BUTTONS
tk.Button(page1,text="Save",command=login).pack(pady=5)


tk.Button(page1,text="Update",command=update_user).pack(pady=5)


# NEXT PAGE BUTTON
tk.Button(page1,text="Next Page",command=open_page2).pack(pady=20)


# RESULT LABEL
result_label = tk.Label(page1, text="")
result_label.pack()


page1.pack(fill="both", expand=True)


# PAGE 2

page2 = tk.Frame(window)

tk.Label(page2,text="ALL USERS",font=("Arial", 18)).pack(pady=10)


# DISPLAY USERS HERE
display_frame = tk.Frame(page2)
display_frame.pack(fill="both", expand=True)


# BACK BUTTON
tk.Button(page2,text="Back",command=back_page).pack(pady=10)


window.mainloop()