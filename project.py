from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
#from PIL import Image, ImageTk
#from tkinter import combobox
import pyttsx3
import os
import threading
import PyPDF2

root = Tk()
root.geometry("1020x530")
root.title("Text to Speech Converter")
root.resizable(False,False)
root.configure(bg="#4187c7")





engine = pyttsx3.init()

global i,j

def speaknow():
    Text = Text_area.get(1.0, END)
    Gender = gender.get()
    Speed = speed.get()
    voices = engine.getProperty('voices')
    engine.setProperty('volume', (slider.get()) / 100)
    Lan = lan.get()
    i = 0
    j = 3

    def setvoice():
        if (Gender == 'Male'):
            engine.setProperty('voice', voices[i].id)
            engine.say(Text)
            engine.runAndWait()
            engine.stop()
        else:
            engine.setProperty('voice', voices[j].id)
            engine.say(Text)
            engine.runAndWait()
            engine.stop()

    if Lan == "Hindi":
        i = 2
        j = 1

    if len(Text) > 1:
        if (Speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif (Speed == "Normal"):
            engine.setProperty('rate', 170)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()

    else:
        messagebox.showwarning("Warning", "First Enter Some Text")


def download():
    Text = Text_area.get(1.0, END)
    Gender = gender.get()
    Speed = speed.get()
    voices = engine.getProperty('voices')
    Lan = lan.get()
    
    i = 0
    j = 3

    if Lan == "Hindi":
        i = 2
        j = 1

    def setvoice():
        if (Gender == 'Male'):
            engine.setProperty('voice', voices[i].id)
            Filename = filedialog.asksaveasfilename(defaultextension=".mp3")
            engine.save_to_file(Text, Filename)
            messagebox.showinfo('Successfull', 'Audio is Saved')
            engine.runAndWait()
            engine.stop()
        else:
            engine.setProperty('voice', voices[j].id)
            Filename = filedialog.asksaveasfilename(defaultextension=".mp3")
            engine.save_to_file(Text, Filename)
            messagebox.showinfo('Successfull', 'Audio is Saved')
            engine.runAndWait()
            engine.stop()

    if len(Text) > 1:

        if (Speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif (Speed == "Normal"):
            engine.setProperty('rate', 170)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()
    else:
        messagebox.showwarning("Warning", "First Enter Some Text")


def open_pdf():
    pdffile = filedialog.askopenfilename()
    pdffile = open(pdffile, 'rb')

    readpdf = PyPDF2.PdfReader(pdffile)

    for i in range(0, len(readpdf.pages)):
        page = readpdf.pages[i]
        TExt = page.extract_text()
        Text_area.insert(END, TExt)

    pdffile.close()


def open_file():
    Text_file = filedialog.askopenfilename(title="open file")
    Text_file = open(Text_file, 'r')
    Text = Text_file.read()

    Text_area.insert(END, Text)
    Text_file.close()




Top_Frame=Frame(root,bg="#FFE45C",width=1100,height=90)
Label(Top_Frame,text="~Text To Speech Converter~",font="Constantia 45 italic",bg="#FFE45C",fg="black").place(x=180,y=10)
Top_Frame.place(x=0,y=0)

Label(root,text="Enter The Text",font="Constantia 20 bold",bg="white",fg="black").place(x=150,y=100)



scrol_bar= Scrollbar(root, orient=VERTICAL)
scrol_bar.place(x=510, y=150, width=16, height=300)
# Text Box
Text_area = Text(root, font="Rpbote 20", bg="white", yscrollcommand=scrol_bar.set, relief=GROOVE, wrap=WORD)
Text_area.place(x=10, y=150, width=500, height=300)
scrol_bar.config(command=Text_area.yview())


# To change the Gender of the Voice
gender = ttk.Combobox(root, values=['Male', 'Female'], font="Constantia 14", state='readonly', width=8)
gender.place(x=550, y=220)
gender.set('Male')

# To Change the Rate of Voice
speed = ttk.Combobox(root, values=['Slow', 'Normal', 'Fast'], font="Constantia 14", state='readonly', width=9)
speed.place(x=710, y=220)
speed.set('Normal')

# To Change Language
lan = ttk.Combobox(root, values=['English', 'Hindi'], font="Constantia 14", state='readonly', width=7)
lan.place(x=870, y=220)
lan.set('English')

# Labels

#label Voice
Label(root, text="VOICE", font="Constantia 20 bold", bg= "#4187c7", fg="black").place(x=550, y=160)

#label Speed
Label(root, text="SPEED", font="Constantia 20 bold", bg= "#4187c7", fg="black").place(x=710, y=160)

#label Volume
Label(root, text="VOLUME", font="Constantia 20 bold", bg= "#4187c7", fg="black").place(x=820, y=300)

#label language
Label(root, text="LANGUAGE", font="Constantia 18 bold", bg= "#4187c7", fg="black").place(x=850, y=160)







# Speak Button
s_btn = Button(root, text="Speak", width=8, height=1, font="Constantia 17 bold", bg='white', activebackground='#c72c2c', relief=SUNKEN,
               bd=5, command=lambda: threading.Thread(target=speaknow, daemon=True).start())
s_btn.place(x=600, y=330)


# Download button
d_btn = Button(root, text='Download', width=10, font='Constantia 17 bold ', relief=SUNKEN, bg='White',
               activebackground='#c72c2c', bd=5, command=download)
d_btn.place(x=580, y=430)

# clear Button to clear text
c_btn = Button(root, text='Clear', width=10,height=1, font='Constantia 17 bold ', relief=SUNKEN, bg='white', activebackground='#c72c2c',
               bd=5, command=lambda: Text_area.delete(0.0, END))
c_btn.place(x=800, y=430)

#Volume
slider = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',
    # horizontal
)
slider.place(x=830 ,y=350)
slider.set(50)

#import file
s_btn=Button(root,text="Import text file",width=13,font="Constantia 16 bold",bg='white',activebackground='#c72c2c',relief=SUNKEN,bd=5,command=open_file)
s_btn.place(x=20 ,y=470)

#import pdf
s_btn=Button(root,text="Import pdf",width=10,font="Constantia 16 bold",bg='white',activebackground='#c72c2c',relief=SUNKEN,bd=5,command=open_pdf)
s_btn.place(x=260 ,y=470)







root.mainloop()