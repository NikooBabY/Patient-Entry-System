from tkinter import *
from tkinter import messagebox

from PIL import Image
from tkinter import ttk
import csv

image = Image.open("Cover.png")
pic = image.resize((1000, 800))
pic.save('Cover1.png')

root = Tk()
root.title("Hospital Patient Entry")
root.geometry("1000x800+250+0")
root.minsize(1000, 800)
root.maxsize(1000, 800)
root.iconbitmap("Hospital.ico")
pic = PhotoImage(file='Cover1.png')


def fun():
    uname = e1.get()  # using get to take value from entry widget
    pwd = e2.get()
    if uname == "test" and pwd == "123":
        root2 = Toplevel()
        root2.title("Hospital Patient Entry")
        root2.geometry("1000x800+250+0")
        root2.minsize(1000, 800)
        root2.maxsize(1000, 800)
        root2.iconbitmap("Hospital.ico")

        photo = PhotoImage(file='cover2.png')
        l2.config(text="Logged In", fg='yellow', bg='#99bbc5', font=("Serif", 35, "bold"))
        b1.config(text="Re-login")

        l5 = Label(root2, image=photo)  # using background image for second window
        l5.image = photo
        l5.pack()

        l6 = Label(root2, text="Patient Entry", fg='Black', bg='#e0efec', font=("Serif", 25, "bold"))
        l6.place(relx='0.5', rely='0.1', anchor='center')

        l7 = Label(root2, text="Patient ID: ", fg='Black', bg='#e1f0ed', font=("Serif", 15, "bold"))
        l8 = Label(root2, text="Name: ", fg='Black', bg='#e1f0ed', font=("Serif", 15, "bold"))
        l9 = Label(root2, text="Sex: ", fg='Black', bg='#e1f0ed', font=("Serif", 15, "bold"))
        l10 = Label(root2, text="Age: ", fg='Black', bg='#e1f0ed', font=("Serif", 15, "bold"))
        l11 = Label(root2, text="Address: ", fg='Black', bg='#e1f0ed', font=("Serif", 15, "bold"))
        l12 = Label(root2, text="Health Issue: ", fg='Black', bg='#e1f0ed', font=("Serif", 15, "bold"))
        l13 = Label(root2, text="Contact: ", fg='Black', bg='#e1f0ed', font=("Serif", 15, "bold"))
        l14 = Label(root2, text="Referred by: ", fg='Black', bg='#e1f0ed', font=("Serif", 15, "bold"))
        l7.place(relx='0.13', rely='0.25')
        l8.place(relx='0.13', rely='0.3')
        l9.place(relx='0.13', rely='0.35')
        l10.place(relx='0.13', rely='0.4')
        l11.place(relx='0.13', rely='0.45')
        l12.place(relx='0.13', rely='0.5')
        l13.place(relx='0.13', rely='0.70')
        l14.place(relx='0.13', rely='0.75')

        e3 = ttk.Entry(root2)
        e3.place(relx='0.30', rely='0.25', relwidth='0.45')
        e4 = ttk.Entry(root2,)
        e4.place(relx='0.30', rely='0.30', relwidth='0.45')

        e5 = ttk.Combobox(root2)
        e5['values'] = ['Male', 'Female']
        e5.place(relx='0.30', rely='0.35', relwidth='0.45')
        e5.current()

        e6 = ttk.Entry(root2)
        e6.place(relx='0.30', rely='0.40', relwidth='0.45')
        e7 = ttk.Entry(root2)
        e7.place(relx='0.30', rely='0.45', relwidth='0.45')
        e8 = Text(root2, insertborderwidth='0.45', relief="groove")
        e8.place(relx='0.30', rely='0.50', relwidth='0.45', relheight='0.15')
        e9 = ttk.Entry(root2)
        e9.place(relx='0.30', rely='0.70', relwidth='0.45', relheight='0.03')
        e10 = ttk.Entry(root2)
        e10.place(relx='0.30', rely='0.75', relwidth='0.45')

        def file():
            with open('Entry.txt', 'a', newline='') as f:
                writer = csv.writer(f)

                a = e3.get()
                b = e4.get()
                c = e5.get()
                d = e6.get()
                e = e7.get()
                f = e8.get("1.0", "end-1c")
                g = e9.get()
                h = e10.get()
                data = [a, b, c, d, e, f, g, h]
                writer.writerow(data)

        def all():
            iden = e3.get()
            age = e6.get()
            contact = e9.get()
            try:
                if int(iden) < 0 and int(age) < 0 and int(contact) < 0:
                    msg = 'Enter valid terms.'
                else:
                    msg = 'Details saved successfully'
                    file()
            except ValueError:
                msg = 'Enter valid terms'
            messagebox.showinfo('Info', msg)

        b3 = ttk.Button(root2, text='Save', command=all)
        b3.place(relx='0.45', rely='0.85')

        frame2 = Frame(root2)
        frame2.pack()

        def third():
            root3 = Toplevel()
            root3.title("Patient Details")
            root3.geometry("620x500+450+150")
            with open("Entry.txt", newline="") as file:
                reader = csv.reader(file)
                # r and c shows where to grid the labels
                r = 0
                for col in reader:
                    c = 0
                    for row in col:
                        label = Label(root3, width=10, height=2, text=row, relief=RIDGE)
                        label.grid(row=r, column=c)
                        c += 1
                    r += 1

            root3.mainloop()

        def deletion():
            root4 = Toplevel()
            root4.title("Delete Details")
            root4.geometry("350x150+600+300")
            root4.maxsize(350, 150)
            root4.minsize(350, 150)

            l15 = Label(root4, text='Enter Patient ID to delete: ')
            l15.place(relx='0.30', rely='0.25')
            e11 = Entry(root4)
            e11.place(relx='0.33', rely='0.50')

            def main():
                updatedlist = []
                with open("Entry.txt", newline="") as f:
                    reader = csv.reader(f)
                    Patient_ID = e11.get()
                    try:
                        Id = int(Patient_ID)
                    except ValueError:
                        messagebox.showerror('Error', "Use valid numbers.")

                    for row in reader:

                        if row[0] == Patient_ID:
                            message = 'Deleted successfully'
                        else:
                            message = 'No patient of that ID'
                        messagebox.showinfo('Info', message)

                        if row[0] != Patient_ID:
                            updatedlist.append(row)
                    updatefile(updatedlist)

            def updatefile(updatedlist):
                with open("Entry.txt", "w", newline="") as f:
                    Writer = csv.writer(f)
                    Writer.writerows(updatedlist)

            b6 = ttk.Button(root4, text='Delete', command=main)
            b6.place(relx='0.40', rely='0.75')

            root4.mainloop()

        b4 = ttk.Button(root2, text="View Patient Details", command=third)
        b4.place(relx='0.867', rely='0.90')

        b5 = ttk.Button(root2, text="Delete Patient Details", command=deletion)
        b5.place(relx='0.86', rely='0.93')

        frame2 = Frame(root2)
        frame2.pack()

    elif uname == "" and pwd == "":
        messagebox.showerror("Blank", 'Please enter info')
    else:
        messagebox.showerror("Failed", 'Wrong Credentials.''Please try again\n')


l1 = Label(root, image=pic)
l1.pack()
l2 = Label(root, text="WELCOME", fg='yellow', bg='#99bbc5', font=("Serif", 35, "bold"))
l2.place(relx='0.25', rely='0.125', anchor='center')

l3 = Label(root, text="Username: ", bg='#a4c0cb', font=("Serif", 15, "bold"))
l3.place(relx='0.13', rely='0.35')
l4 = Label(root, text="Password: ", bg='#a3c1cb', font=("Serif", 15, "bold"))
l4.place(relx='0.13', rely='0.4')
e1 = Entry(root)
e1.place(relx='0.25', rely='0.35', height='27')
e2 = Entry(root, show='*')
e2.place(relx='0.25', rely='0.4', height='27')
b1 = ttk.Button(root, text="Submit", command=fun)
b1.place(relx='0.21', rely='0.45')
b2 = ttk.Button(root, text="Quit", command=root.quit)
b2.place(relx='0.21', rely='0.5')

frame1 = Frame(root)
frame1.pack()

root.mainloop()
