import tkinter as tk
import sqlite3

# Create the database connection
conn = sqlite3.connect('login.db')
c = conn.cursor()

# Create the tables
c.execute('CREATE TABLE user2 (username text, password text)')

# Create the main window
root = tk.Tk()
root.title('Signup and Login')

# Create the frames
signup_frame = tk.Frame(root)
login_frame = tk.Frame(root)

# Create the widgets for the signup frame
username_label = tk.Label(signup_frame, text='Username:')
username_entry = tk.Entry(signup_frame)
username_entry.focus()
password_label = tk.Label(signup_frame, text='Password:')
password_entry = tk.Entry(signup_frame, show='*')
confirm_password_label = tk.Label(signup_frame, text='Confirm Password:')
confirm_password_entry = tk.Entry(signup_frame, show='*')
signup_button = tk.Button(signup_frame, text='Signup', command=lambda:signup)

# Create the widgets for the login frame
username_label_login = tk.Label(login_frame, text='Username:')
username_entry_login = tk.Entry(login_frame)
password_label_login = tk.Label(login_frame, text='Password:')
password_entry_login = tk.Entry(login_frame, show='*')
login_button = tk.Button(login_frame, text='Login', command=lambda:login)

# Add validations to the signup form
def validate_username(username):
  if len(username) < 3:
    return False
  else:
    return True

def validate_password(password):
  if len(password) < 8:
    return False
  else:
    return True

def validate_confirm_password(password, confirm_password):
  if password != confirm_password:
    return False
  else:
    return True

# Pack the widgets
signup_frame.pack()
login_frame.pack()

# Mainloop
root.mainloop()

def signup():
  # Get the username and password from the user
  username = username_entry.get()
  password = password_entry.get()
  confirm_password = confirm_password_entry.get()

  # Validate the username and password
  if not validate_username(username):
    tk.messagebox.showerror('Error', 'Username must be at least 3 characters long')
    return

  if not validate_password(password):
    tk.messagebox.showerror('Error', 'Password must be at least 8 characters long')
    return

  if not validate_confirm_password(password, confirm_password):
    tk.messagebox.showerror('Error', 'Passwords do not match')
    return

  # Check if the username already exists
  c.execute('SELECT * FROM user2 WHERE username = ?', (username,))
  if c.fetchone():
    tk.messagebox.showerror('Error', 'Username already exists')
    return

  # Insert the new user into the database
  c.execute('INSERT INTO user2 (username, password) VALUES (?, ?)', (username, password))
  conn.commit()

  # Notify the user that they have successfully signed up
  tk.messagebox.showinfo('Success', 'You have successfully signed up')

def login():
  # Get the username and password from the user
  username = username_entry_login.get()
  password = password_entry_login.get()

  # Check if the username and password are correct
  c.execute('SELECT * FROM user2 WHERE username = ? AND password = ?', (username, password))
  if not c.fetchone():
    tk.messagebox.showerror('Error', 'Invalid username or password')
    return

  # Notify the user that they have successfully logged in
  tk.messagebox.showinfo('Success', 'You have successfully logged in')
