from tkinter import *
from turtle import width
from tkhtmlview import HTMLLabel
root = Tk()
root.geometry("903x600")
root.title("Teste HTML")
root.config(bg='#8a37cc')

# creditos
# <a href='https://br.freepik.com/fotos-vetores-gratis/fachada-de-vidro'>Fachada de vidro foto criado por diana.grytsku - br.freepik.com</a>


# Title = HTMLLabel(root, html="<h1>Banco Farefaith</h1>").grid(row=0, column=0)

fr1 = LabelFrame(root).grid()

Title = Label(fr1, text="Banco qweojbk", font=("Mongolian Baiti", "25"),bg='#8a37cc', fg="#f5f5f5").grid(row=0, column=0, sticky=W, pady=15)

cadastre = Button(fr1, text=" Cadastre-se ", bg="#eb8334", fg="#fff",width=15, height=1).place(bordermode=OUTSIDE, x=540, y=26)
logar = Button(fr1, text=" Faça Login ", bg="#eb8334", fg="#fff",width=15, height=1).place(bordermode=OUTSIDE, x=660, y=26)
about = Button(fr1, text=" Sobre nós ", bg="#eb8334", fg="#fff",width=15, height=1).place(bordermode=OUTSIDE, x=780, y=26)

photo = HTMLLabel(fr1, html="<img src='chance.png'>", width=112,background='#8a37cc').grid(row=1, column=0, columnspan=4)

about1 = HTMLLabel(root, html="<h2>Quem Somos?</h2>", background='#8a37cc',foreground='#f5f5f5').place(bordermode=OUTSIDE, x=320, y=360)

about2 = HTMLLabel(root, html="<p>aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa</p>",background='#8a37cc',foreground='#f5f5f5').place(bordermode=OUTSIDE, x=250, y=400)


root.mainloop()
