from tkinter import *
from tkhtmlview import HTMLLabel
root = Tk()
root.geometry("500x600")
root.title("Teste HTML")


my_label = HTMLLabel(root, html="\
    <h1>HelloWorld</h1>\
    <br>\
    <p> oi </p>\
    <p style='color: green;'>oi</p>").grid()










root.mainloop()