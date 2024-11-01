import tkinter
import pyttsx3
from PyPDF2 import PdfReader
from tkinter import Tk, Label, Button, Radiobutton, Scale
from tkinter.filedialog import askopenfilename


# initializing the tts
voice = pyttsx3.init()
voice.setProperty('volume', 1.0)


def setspeed():
    spd = speed.get()
    voice.getProperty('rate')
    voice.setProperty('rate', spd)


def gender(num):
    num = num.get()
    voices = voice.getProperty('voices')
    voice.setProperty('voice', voices[num].id)


# function that allows a user to select a pdf from their files and have it automatically be read to them
def readtome():
    text = PdfReader(askopenfilename())

    book_length = list(text.pages)

    billy_sol_estes = []

    for i in book_length:
        page = i.extract_text()
        billy_sol_estes.append(page)

    for page in billy_sol_estes:
        voice.say(page)
        voice.runAndWait()


# initializing tkinter window
window = Tk()
window.geometry('400x400')

num = tkinter.IntVar()

titletext = Label(text='Read To Me Text-To-Speech PDF Reader', font=('Lato', 15))
titletext.pack()

male = Radiobutton(text='Male Voice', variable=num, value=0)
male.pack(pady=10)

female = Radiobutton(text='Female Voice', variable=num, value=1)
female.deselect()
female.pack()

voicechange = Button(text='Change Voice', command=lambda: gender(num))
voicechange.pack(pady=15)

speedlabel = Label(text='Change Voice Speed', font=(10))
speedlabel.pack()

speed = Scale(orient="horizontal", length=320, from_=1, to=500)
speed.pack()

changespd = Button(text='Save Voice Speed', command=setspeed)
changespd.pack(pady=7)

fileselect = Button(text='Select PDF', command=readtome)
fileselect.pack(pady=10)

note = Label(text='Note: Reading will begin as soon as a PDF file is selected.', font=('Minion Pro SmBd', 10, 'bold'))
note.pack(pady=10)

window.mainloop()