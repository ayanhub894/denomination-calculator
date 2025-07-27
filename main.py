from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk

window = Tk()
window.title("Denomination Calculator")
window.configure(bg="lightblue")
window.geometry("700x900")

image = Image.open("deno.png")
upload_resize = image.resize((400, 300))
tkimage = ImageTk.PhotoImage(upload_resize)

upload = Label(window, image=tkimage, bg="lightblue")
upload.place(x=150, y=100)  # Centered horizontally

intro_label = Label(window, text="Welcome to the Denomination Calculator", bg="lightblue", font=("Arial", 16))
intro_label.place(x=150, y=30)

def msgbox():
    answer = messagebox.showinfo("Alert", "Do you want to continue?")
    if answer == "ok":
        top()

button = Button(window, text="Click to continue", command=msgbox, bg="lightblue", fg="blue")
button.place(x=250, y=420)

def top():
    global t_entry, t_entry_2000, t_entry_500, t_entry_100
    global top_window
    top_window = Toplevel(window)
    top_window.title("Denomination Calculator")
    top_window.geometry("500x400")
    top_window.configure(bg="blue")

    t_label = Label(top_window, text="Enter the amount", bg="blue", fg="white", font=("Arial", 12))
    t_label.place(x=50, y=30)
    t_entry = Entry(top_window)
    t_entry.place(x=200, y=30)

    t_label_2000 = Label(top_window, text="Notes of 2000:", bg="blue", fg="white")
    t_label_2000.place(x=50, y=80)
    t_entry_2000 = Entry(top_window)
    t_entry_2000.place(x=200, y=80)

    t_label_500 = Label(top_window, text="Notes of 500:", bg="blue", fg="white")
    t_label_500.place(x=50, y=130)
    t_entry_500 = Entry(top_window)
    t_entry_500.place(x=200, y=130)

    t_label_100 = Label(top_window, text="Notes of 100:", bg="blue", fg="white") 
    t_label_100.place(x=50, y=180)
    t_entry_100 = Entry(top_window)
    t_entry_100.place(x=200, y=180) 
    calculate_button = Button(top_window, text="Calculate", command=calculate, bg="blue", fg="black")
    calculate_button.place(x=200, y=230)
def calculate():
    try:
            amount = int(t_entry.get())
            notes_2000 = amount // 2000
            amount %= 2000
            notes_500 = amount // 500
            amount %= 500
            notes_100 = amount // 100
            t_entry_2000.delete(0, END)
            t_entry_500.delete(0, END)
            t_entry_100.delete(0, END)
            t_entry_2000.insert(0, str(notes_2000))
            t_entry_500.insert(0, str(notes_500))
            t_entry_100.insert(0, str(notes_100))
    except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")

    

window.mainloop() 
