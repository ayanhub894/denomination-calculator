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
    global t_entry, t_entry_5000, t_entry_500, t_entry_100, t_entry_50, t_entry_20, t_entry_10, t_entry_1000
    global top_window
    top_window = Toplevel(window)
    top_window.title("Denomination Calculator")
    top_window.geometry("700x500")
    top_window.configure(bg="blue")

    t_label = Label(top_window, text="Enter the amount", bg="blue", fg="white", font=("Arial", 12))
    t_label.place(x=50, y=30)
    t_entry = Entry(top_window)
    t_entry.place(x=200, y=30)

    t_label_5000 = Label(top_window, text="Notes of 5000:", bg="blue", fg="white")
    t_label_5000.place(x=50, y=80)
    t_entry_5000 = Entry(top_window)
    t_entry_5000.place(x=200, y=80)

    t_label_500 = Label(top_window, text="Notes of 500:", bg="blue", fg="white")
    t_label_500.place(x=50, y=130)
    t_entry_500 = Entry(top_window)
    t_entry_500.place(x=200, y=130)

    t_label_100 = Label(top_window, text="Notes of 100:", bg="blue", fg="white") 
    t_label_100.place(x=50, y=180)
    t_entry_100 = Entry(top_window)
    t_entry_100.place(x=200, y=180)  
    
    t_label_50 = Label(top_window, text="Notes of 50:", bg="blue", fg="white") 
    t_label_50.place(x=50, y=230)
    t_entry_50 = Entry(top_window)
    t_entry_50.place(x=200, y=230)  

    
    t_label_20 = Label(top_window, text="Notes of 20:", bg="blue", fg="white") 
    t_label_20.place(x=50, y=280)
    t_entry_20 = Entry(top_window)
    t_entry_20.place(x=200, y=280)  

    
    t_label_10 = Label(top_window, text="Notes of 10:", bg="blue", fg="white") 
    t_label_10.place(x=50, y=330)
    t_entry_10 = Entry(top_window)
    t_entry_10.place(x=200, y=330)  

    
    t_label_1000 = Label(top_window, text="Notes of 1000:", bg="blue", fg="white") 
    t_label_1000.place(x=50, y=380)
    t_entry_1000 = Entry(top_window)
    t_entry_1000.place(x=200, y=380)  

    calculate_button = Button(top_window, text="Calculate", command=calculate, bg="blue", fg="black")
    calculate_button.place(x=200, y=430)
def calculate():
    try:
            amount = int(t_entry.get())
            notes_5000 = amount // 5000
            amount %= 5000
            notes_500 = amount // 500
            amount %= 500
            notes_100 = amount // 100 
            amount %= 100
            notes_50 = amount // 50     
            amount %= 50
            notes_20 = amount // 20
            amount %= 20
            notes_10 = amount // 10
            amount %= 10
            notes_1000 = amount // 1000
            amount %= 1000
            t_entry_5000.delete(0, END)
            t_entry_500.delete(0, END)
            t_entry_100.delete(0, END)
            t_entry_5000.insert(0, str(notes_5000))
            t_entry_500.insert(0, str(notes_500))
            t_entry_100.insert(0, str(notes_100)) 
            t_entry_50.insert(0, str(notes_50))
            t_entry_20.insert(0, str(notes_20))
            t_entry_10.insert(0, str(notes_10))
            t_entry_1000.insert(0, str(notes_1000))
    except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")

    

window.mainloop() 
