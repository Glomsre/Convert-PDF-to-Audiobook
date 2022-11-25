from tkinter import *
import pyttsx3
import PyPDF2
from PyPDF2 import PdfFileReader

voice = pyttsx3.init()
voice.setProperty('rate', 125)


def read_pdf():

    data = input_path.get()
    my_file = open(data, 'rb')
    reader = PdfFileReader(my_file)
    number_of_pages = reader.numPages

    for i in range(0, number_of_pages):
        page = reader.getPage(i)
        text = page.extractText()
        voice.say(text)
        voice.runAndWait()

    my_file.close()


window = Tk()
window.title("Convert PDF to Audiobook")
window.config(padx=50, pady=50, bg='#000000')

label_path = Label(text='PDF Path', bg='#000000', fg='#ffffff', font=('Helvetica', 20))
label_path.grid(column=1, row=1, padx=10)
input_path = Entry(window, width=30, font=('Helvetica', 20))
input_path.grid(column=2, row=1, padx=10)
button_open = Button(window, text="Read", command=read_pdf, bg='#000000', fg='#ffffff', font=('Helvetica', 20))
button_open.grid(column=3, row=1)

window.mainloop()
