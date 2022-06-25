from tkinter import *
from turtle import width
from tkhtmlview import HTMLLabel
root = Tk()
root.geometry("904x600+200+50")
root.title("Teste HTML")
root.config(bg='#8a37cc')

# creditos
# <a href='https://br.freepik.com/fotos-vetores-gratis/fachada-de-vidro'>Fachada de vidro foto criado por diana.grytsku - br.freepik.com</a>


#---------------------- Frame 1 / index ----------------------#

# fr1 = LabelFrame(root).grid()

# Title = HTMLLabel(fr1, html="<h1 style ='color:#f5f5f5;font:Mongolian Baiti;'>Banco Farefaith</h1>",background='#8a37cc').place(bordermode=OUTSIDE, x=45, y=15)

# cadastre = Button(fr1, text=" Cadastre-se ", bg="#eb8334", fg="#fff",width=18, height=2).place(bordermode=OUTSIDE, x=480, y=28)
# logar = Button(fr1, text=" Faça Login ", bg="#eb8334", fg="#fff",width=18, height=2).place(bordermode=OUTSIDE, x=620, y=28)
# about = Button(fr1, text=" Área funcionario ", bg="#eb8334", fg="#fff",width=18, height=2).place(bordermode=OUTSIDE, x=760, y=28)

# photo = HTMLLabel(fr1, html="<img src='chance.png'>", width=112,background='#8a37cc').place(bordermode=OUTSIDE, x=0, y=100)

# about1 = HTMLLabel(fr1, html="<h2 style ='color:#f5f5f5;font:Mongolian Baiti;'>Quem Somos?</h2>", background='#8a37cc',foreground='#f5f5f5').place(bordermode=OUTSIDE, x=320, y=360)
# about2 = HTMLLabel(fr1, html="<p style ='color:#f5f5f5;font:Mongolian Baiti; font-size:15px;'>Lorem ipsum dolor sit amet, consectetur adipiscing elit\
# Aenean volutpat neque mi, at finibus felis volutpat ut\
# Interdum et malesuada fames ac ante ipsum primis in faucibus.</p>",background='#8a37cc').place(bordermode=OUTSIDE, x=120, y=420)


#---------------------- Frame 2 / Cadastro user ----------------------#

# fr2 = LabelFrame(root).grid()

# Title_fr2 = HTMLLabel(fr2, html="<h1 style ='color:#f5f5f5;font:Mongolian Baiti;'>Cadastre-se agora</h1>",background='#8a37cc').place(bordermode=OUTSIDE, x=45, y=15)

# cadastre_fr2 = Button(fr2, text=" Voltar ", bg="#eb8334", fg="#fff",width=18, height=2).place(bordermode=OUTSIDE, x=480, y=28)
# logar_fr2 = Button(fr2, text=" Faça Login ", bg="#eb8334", fg="#fff",width=18, height=2).place(bordermode=OUTSIDE, x=620, y=28)
# about_fr2 = Button(fr2, text=" Área funcionario ", bg="#eb8334", fg="#fff",width=18, height=2).place(bordermode=OUTSIDE, x=760, y=28)

# info_fr2 = HTMLLabel(fr2, html="<h5 style ='color:#f5f5f5;font:Mongolian Baiti;'>Complete todos os campos a seguir </h5>",background='#8a37cc').place(bordermode=OUTSIDE, x=45, y=103)

# form_fr2 = HTMLLabel(fr2, html="<img src='meus.png'>", width=112, height=27,background='#8a37cc').place(bordermode=OUTSIDE, x=40, y=143)

# #Entrada de dados

# nome_fr2 = Entry(fr2, bg="#eb8334",width=55, font='Arial 18').place(bordermode=OUTSIDE, x=140, y=236)

# cpf_fr2 = Entry(fr2, bg="#eb8334",width=27, font='Arial 18').place(bordermode=OUTSIDE, x=140, y=285)

# date_fr2 = Entry(fr2, bg="#eb8334",width=20, font='Arial 18').place(bordermode=OUTSIDE, x=596, y=285)

# civil_fr2 = Entry(fr2, bg="#eb8334",width=24, font='Arial 18').place(bordermode=OUTSIDE, x=178, y=339)

# tel_fr2 = Entry(fr2, bg="#eb8334",width=20, font='Arial 18').place(bordermode=OUTSIDE, x=596, y=339)

# logradouro_fr2 = Entry(fr2, bg="#eb8334",width=24, font='Arial 18').place(bordermode=OUTSIDE, x=178, y=391)

# num_fr2 = Entry(fr2, bg="#eb8334",width=23, font='Arial 18').place(bordermode=OUTSIDE, x=558, y=391)

# bairro_fr2 = Entry(fr2, bg="#eb8334",width=27, font='Arial 18').place(bordermode=OUTSIDE, x=140, y=443)

# city_fr2 = Entry(fr2, bg="#eb8334",width=22, font='Arial 18').place(bordermode=OUTSIDE, x=570, y=442)

# email_fr2 = Entry(fr2, bg="#eb8334",width=27, font='Arial 18').place(bordermode=OUTSIDE, x=140, y=500)

# passw_fr2 = Entry(fr2, bg="#eb8334",width=22, font='Arial 18').place(bordermode=OUTSIDE, x=570, y=500)

#---------------------- Frame 3 / Login ----------------------#

root.mainloop()
