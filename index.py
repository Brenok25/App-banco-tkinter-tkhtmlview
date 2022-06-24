from tkinter import *
from tkhtmlview import HTMLLabel
root = Tk()
root.geometry("500x600")
root.title("Teste HTML")


my_label = HTMLLabel(root, html=" <h1>HelloWorld</hi>").grid()










root.mainloop()