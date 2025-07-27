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
tkimage = ImageTk.PhotoImage(image) 

upload = Label(window, image=tkimage, bg="lightblue")  
upload.place(x=0, y=300)

intro_label = Label(window, text="Welcome to the Denomination Calculator",bg="Light blue") 
intro_label.place(x=0, y=-100)   

def msgbox(): 
    answer = messagebox.showinfo("Alert", "Do you want to continue?") 
    if answer == "ok": 
        top() 

button = Button(window, text="Click to continue", command=msgbox, bg="lightblue", fg="blue")  
button.place(x=0, y=-150, ANCHOR=CENTER) 

def top():  
    global t_entry, t_entry_2000, t_entry_500, t_entry_100, top_window
    top_window = Toplevel() 
    top_window.title("Denomination Calculator") 
    top_window.geometry("500x700") 
    top_window.configure(bg="blue") 
    t_label = Label(top_window, text="Enter the amount") 
    t_label.place(x=-100, y=100) 
    t_entry = Entry(top_window) 
    t_entry.place(x=-100,y=75) 
    t_label_2000 = Label(top_window, text="notes of 2000:", bg="blue")  
    t_label_2000.place(x=-100, y=50) 
    t_entry_2000 = Entry(top_window)  
    t_entry_2000.place(x=-100, y=25)
    t_label_500 = Label(top_window, text="notes of 500:", bg="blue")  
    t_label_500.place(x=-100, y=0) 
    t_entry_500 = Entry(top_window)  
    t_entry_500.place(x=-100, y=-25) 

    t_label_100 = Label(top_window, text="notes of 2000:", bg="blue")  
    t_label_100.place(x=-100, y=50) 
    t_entry_100 = Entry(top_window) 
    t_entry_100.place(x=-100, y=-50)  

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
        messagebox.showerror("Error", "please enter a valid amount") 

calculate_button = Button(top_window, text="Calculate", command=calculate,bg="lightblue", fg="black") 
calculate_button.place(x=-100, y=-75)  
top_window.mainloop()
window.mainloop()
        
    






