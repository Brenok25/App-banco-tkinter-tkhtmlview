from tarfile import ExtractError
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

# Title_fr1 = HTMLLabel(fr1, html="<h1 style ='color:#f5f5f5;font:Mongolian Baiti;'>Banco Farefaith</h1>",background='#8a37cc').place(bordermode=OUTSIDE, x=45, y=15)

# cadastre_fr1 = Button(fr1, text=" Cadastre-se ", bg="#eb8334", fg="#fff",width=18, height=2).place(bordermode=OUTSIDE, x=480, y=28)
# logar_fr1 = Button(fr1, text=" Faça Login ", bg="#eb8334", fg="#fff",width=18, height=2).place(bordermode=OUTSIDE, x=620, y=28)
# func_fr1 = Button(fr1, text=" Área funcionario ", bg="#eb8334", fg="#fff",width=18, height=2).place(bordermode=OUTSIDE, x=760, y=28)

# photo_fr1 = HTMLLabel(fr1, html="<img src='fr1.png'>", width=112,background='#8a37cc').place(bordermode=OUTSIDE, x=0, y=100)

# about1_fr1 = HTMLLabel(fr1, html="<h2 style ='color:#f5f5f5;font:Mongolian Baiti;'>Quem Somos?</h2>", background='#8a37cc',foreground='#f5f5f5').place(bordermode=OUTSIDE, x=320, y=360)
# about2_fr1 = HTMLLabel(fr1, html="<p style ='color:#f5f5f5;font:Mongolian Baiti; font-size:15px;'>Lorem ipsum dolor sit amet, consectetur adipiscing elit\
# Aenean volutpat neque mi, at finibus felis volutpat ut\
# Interdum et malesuada fames ac ante ipsum primis in faucibus.</p>",background='#8a37cc').place(bordermode=OUTSIDE, x=120, y=420)


#---------------------- Frame 2 / Cadastro user ----------------------#

# fr2 = LabelFrame(root).grid()

# Title_fr2 = HTMLLabel(fr2, html="<h1 style ='color:#f5f5f5;font:Mongolian Baiti;'>Cadastre-se agora</h1>",background='#8a37cc').place(bordermode=OUTSIDE, x=45, y=15)

# voltar_fr2 = Button(fr2, text=" Voltar ", bg="#eb8334", fg="#fff",width=18, height=2).place(bordermode=OUTSIDE, x=480, y=28)
# logar_fr2 = Button(fr2, text=" Faça Login ", bg="#eb8334", fg="#fff",width=18, height=2).place(bordermode=OUTSIDE, x=620, y=28)
# func_fr2 = Button(fr2, text=" Área funcionario ", bg="#eb8334", fg="#fff",width=18, height=2).place(bordermode=OUTSIDE, x=760, y=28)

# info_fr2 = HTMLLabel(fr2, html="<h5 style ='color:#f5f5f5;font:Mongolian Baiti;'>Complete todos os campos a seguir </h5>",background='#8a37cc').place(bordermode=OUTSIDE, x=45, y=103)

# form_fr2 = HTMLLabel(fr2, html="<img src='fr2.png'>", width=112, height=27,background='#8a37cc').place(bordermode=OUTSIDE, x=40, y=143)

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

# fr3 = LabelFrame(root).grid()

# Title_fr3 = HTMLLabel(fr3, html="<h1 style ='color:#f5f5f5;font:Mongolian Baiti;'>Faça login!</h1>",
#                       background='#8a37cc').place(bordermode=OUTSIDE, x=45, y=15)

# voltar_fr3 = Button(fr3, text=" Voltar ", bg="#eb8334", fg="#fff",
#                     width=18, height=2).place(bordermode=OUTSIDE, x=480, y=28)

# cadastre_fr3 = Button(fr3, text=" Cadastre-se ", bg="#eb8334", fg="#fff",
#                       width=18, height=2).place(bordermode=OUTSIDE, x=620, y=28)

# func_fr3 = Button(fr3, text="  ", bg="#eb8334", fg="#fff",
#                   width=18, height=2).place(bordermode=OUTSIDE, x=760, y=28)

# form_fr3 = HTMLLabel(fr3, html="<img src='fr3.png'>", width=112, height=27,
#                      background='#8a37cc').place(bordermode=OUTSIDE, x=185, y=120)

# login_fr3 = Entry(fr3, bg="#eb8334", width=17, font='Arial 25').place(
#     bordermode=OUTSIDE, x=290, y=260)

# passw_fr3 = Entry(fr3, bg="#eb8334", width=17, font='Arial 25').place(
#     bordermode=OUTSIDE, x=290, y=375)

# show_fr3 = Button(fr3, text='👁', font=('Mongolian Baiti', "18", "bold"),bg='#eb8334', fg='#fff').place(
#     bordermode=OUTSIDE, x=605, y=374)

# entra_fr3 = Button(fr3, text=" Entrar ", font=('Mongolian Baiti', '15'), bg="#eb8334",
#                    fg="#fff", width=24, height=2).place(bordermode=OUTSIDE, x=307, y=455)

#---------------------- Frame 4 / Home Funcionario ----------------------#

# fr4 = LabelFrame(root).grid()

# Title_fr4 = HTMLLabel(fr4, html="<h1 style ='color:#f5f5f5;font:Mongolian Baiti;'>Home Funcionario</h1>",
#                       background='#8a37cc').place(bordermode=OUTSIDE, x=45, y=15)

# voltar_fr4 = Button(fr4, text=" Voltar ", bg="#eb8334", fg="#fff",
#                     width=18, height=2).place(bordermode=OUTSIDE, x=480, y=28)

# cadastre_fr4 = Button(fr4, text=" Cadastre-se ", bg="#eb8334", fg="#fff",
#                       width=18, height=2).place(bordermode=OUTSIDE, x=620, y=28)

# logar_fr4 = Button(fr4, text=" Login Usuario ", bg="#eb8334", fg="#fff",
#                   width=18, height=2).place(bordermode=OUTSIDE, x=760, y=28)

# cadastrar_user_fr4 = Button(fr4, text=" Cadastrar user ", font=('Mongolian Baiti', '15'), bg="#eb8334",
#                             fg="#fff", width=24, height=2).place(bordermode=OUTSIDE, x=50, y=150)

# deletar_user_fr4 = Button(fr4, text=" Excluir user ", font=('Mongolian Baiti', '15'), bg="#eb8334",
#                           fg="#fff", width=24, height=2).place(bordermode=OUTSIDE, x=50, y=300)

# trocar_infos_fr4 = Button(fr4, text=" Mudar informações ", font=('Mongolian Baiti', '15'), bg="#eb8334",
#                           fg="#fff", width=24, height=2).place(bordermode=OUTSIDE, x=50, y=450)

# about1_fr4 = HTMLLabel(fr4, html="<h2 style ='color:#f5f5f5;font:Mongolian Baiti;'>Informações do Funcionario</h2>",
#                        background='#8a37cc').place(bordermode=OUTSIDE, x=450, y=150

# nome_fr4 = HTMLLabel(fr4, html="<p style ='color:#f5f5f5;font:Mongolian Baiti;'>Nome: Breno Kauan</p>",
#                      background='#8a37cc').place(bordermode=OUTSIDE, x=450, y=230)

# date_fr4 = HTMLLabel(fr4, html="<p style ='color:#f5f5f5;font:Mongolian Baiti;'>Data de Nascimento: 25/04/2003</p>",
#                      background='#8a37cc').place(bordermode=OUTSIDE, x=450, y=270)

# func_fr4 = HTMLLabel(fr4, html="<p style ='color:#f5f5f5;font:Mongolian Baiti;'>Função: Gerenciador de atividade</p>",
#                      background='#8a37cc').place(bordermode=OUTSIDE, x=450, y=310)

# cpf_fr4 = HTMLLabel(fr4, html="<p style ='color:#f5f5f5;font:Mongolian Baiti;'>CPF: 123.123.123-44</p>",
#                      background='#8a37cc').place(bordermode=OUTSIDE, x=450, y=350)

# email_fr4 = HTMLLabel(fr4, html="<p style ='color:#f5f5f5;font:Mongolian Baiti;'>Email: Serhumano321@gamil.com</p>",
#                       background='#8a37cc').place(bordermode=OUTSIDE, x=450, y=390)

# city_fr4 = HTMLLabel(fr4, html="<p style ='color:#f5f5f5;font:Mongolian Baiti;'>Cidade: Pouso Alegre </p>",
#                      background='#8a37cc').place(bordermode=OUTSIDE, x=450, y=430)

# uf_fr4 = HTMLLabel(fr4, html="<p style ='color:#f5f5f5;font:Mongolian Baiti;'>UF: Minas Gerais </p>",
#                      background='#8a37cc').place(bordermode=OUTSIDE, x=450, y=470)

#---------------------- Frame 5 / Usuario ----------------------#

# fr5 = LabelFrame(root).grid()

# Title_fr5 = HTMLLabel(fr5, html="<h1 style ='color:#f5f5f5;font:Mongolian Baiti;'>Home Usuario</h1>",
#                       background='#8a37cc').place(bordermode=OUTSIDE, x=45, y=15)

# voltar_fr5 = Button(fr5, text=" Voltar ", bg="#eb8334", fg="#fff",
#                     width=18, height=2).place(bordermode=OUTSIDE, x=480, y=28)

# cadastre_fr5 = Button(fr5, text=" Cadastre-se ", bg="#eb8334", fg="#fff",
#                       width=18, height=2).place(bordermode=OUTSIDE, x=620, y=28)

# excluir_fr5 = Button(fr5, text=" Excluir Conta ", bg="#eb8334", fg="#fff",
#                    width=18, height=2).place(bordermode=OUTSIDE, x=760, y=28)

# deposito_fr5 = Button(fr5, text=" Deposito ", font=('Mongolian Baiti', '15'), bg="#eb8334",
#                       fg="#fff", width=24, height=2).place(bordermode=OUTSIDE, x=50, y=150)

# saque_fr5 = Button(fr5, text=" Saque ", font=('Mongolian Baiti', '15'), bg="#eb8334",
#                    fg="#fff", width=24, height=2).place(bordermode=OUTSIDE, x=50, y=250)

# trasferencia_fr5 = Button(fr5, text=" Trasferencia ", font=('Mongolian Baiti', '15'), bg="#eb8334",
#                           fg="#fff", width=24, height=2).place(bordermode=OUTSIDE, x=50, y=350)

# extrato_fr5 = Button(fr5, text=" Extrato ", font=('Mongolian Baiti', '15'), bg="#eb8334",
#                      fg="#fff", width=24, height=2).place(bordermode=OUTSIDE, x=50, y=450)

# about1_fr5 = HTMLLabel(fr5, html="<h2 style ='color:#f5f5f5;font:Mongolian Baiti;'>Informações do Usúario</h2>",
#                        background='#8a37cc').place(bordermode=OUTSIDE, x=450, y=150)

# nome_fr5 = HTMLLabel(fr5, html="<p style ='color:#f5f5f5;font:Mongolian Baiti;'> Nome do User </p>",
#                      background='#8a37cc').place(bordermode=OUTSIDE, x=450, y=230)

# date_fr5 = HTMLLabel(fr5, html="<p style ='color:#f5f5f5;font:Mongolian Baiti;'>Data de Nascimento do user</p>",
#                      background='#8a37cc').place(bordermode=OUTSIDE, x=450, y=270)

# cpf_fr5 = HTMLLabel(fr5, html="<p style ='color:#f5f5f5;font:Mongolian Baiti;'> Cpf do user </p>",
#                     background='#8a37cc').place(bordermode=OUTSIDE, x=450, y=310)

# logradouro_fr5 = HTMLLabel(fr5, html="<p style ='color:#f5f5f5;font:Mongolian Baiti;'> Logradouro do user </p>",
#                            background='#8a37cc').place(bordermode=OUTSIDE, x=450, y=350)

# city_fr5 = HTMLLabel(fr5, html="<p style ='color:#f5f5f5;font:Mongolian Baiti;'> Cidade do user </p>",
#                            background='#8a37cc').place(bordermode=OUTSIDE, x=450, y=390)

# email_fr5 = HTMLLabel(fr5, html="<p style ='color:#f5f5f5;font:Mongolian Baiti;'> Email do user </p>",
#                       background='#8a37cc').place(bordermode=OUTSIDE, x=450, y=430)

# saldo_fr5 = HTMLLabel(fr5, html="<p style ='color:#f5f5f5;font:Mongolian Baiti;'> Saldo do user </p>",
#                       background='#8a37cc').place(bordermode=OUTSIDE, x=450, y=470)

# #---------------------- Frame 6 / Home funcionario/ Excluir usuario ----------------------#

# fr6 = LabelFrame(root).grid()

# Title_fr6 = HTMLLabel(fr6, html="<h1 style ='color:#f5f5f5;font:Mongolian Baiti;'>Home Funcionario</h1>",
#                       background='#8a37cc').place(bordermode=OUTSIDE, x=45, y=15)

# voltar_fr6 = Button(fr6, text=" Voltar ", bg="#eb8334", fg="#fff",
#                     width=18, height=2).place(bordermode=OUTSIDE, x=480, y=28)

# logout_fr6 = Button(fr6, text=" Logout ", bg="#eb8334", fg="#fff",
#                     width=18, height=2).place(bordermode=OUTSIDE, x=620, y=28)

# logar_fr6 = Button(fr6, text=" Login Usuario ", bg="#eb8334", fg="#fff",
#                    width=18, height=2).place(bordermode=OUTSIDE, x=760, y=28)

# about1_fr6 = HTMLLabel(fr6, html="<h2 style ='color:#f5f5f5;font:Mongolian Baiti;'>Excluir Usúario</h2>",
#                        background='#8a37cc').place(bordermode=OUTSIDE, x=450, y=150)

# form_fr6 = HTMLLabel(fr6, html="<img src='fr6_fr7.png'>", width=112, height=27,
#                      background='#8a37cc').place(bordermode=OUTSIDE, x=220, y=120)

# cpf_user_fr6 = Entry(fr6, bg="#eb8334", width=17, font='Arial 25').place(
#     bordermode=OUTSIDE, x=285, y=248)

# passw_func__fr6 = Entry(fr6, bg="#eb8334", width=17, font='Arial 25').place(
#     bordermode=OUTSIDE, x=285, y=362)

# show_fr6 = Button(fr6, text='👁', font=('Mongolian Baiti', "18", "bold"), bg='#eb8334', fg='#fff').place(
#     bordermode=OUTSIDE, x=605, y=360)

# entra_fr6 = Button(fr6, text=" Excluir ", font=('Mongolian Baiti', '15'), bg="#eb8334",
#                    fg="#fff", width=24, height=2).place(bordermode=OUTSIDE, x=300, y=455)


#---------------------- Frame 7 / Home Usuario/ Excluir usuario ----------------------#

fr7 = LabelFrame(root).grid()

Title_fr7 = HTMLLabel(fr7, html="<h1 style ='color:#f5f5f5;font:Mongolian Baiti;'>Home Usuario</h1>",
                      background='#8a37cc').place(bordermode=OUTSIDE, x=45, y=15)

voltar_fr7 = Button(fr7, text=" Voltar ", bg="#eb8334", fg="#fff",
                    width=18, height=2).place(bordermode=OUTSIDE, x=480, y=28)

logout_fr7 = Button(fr7, text=" Logout ", bg="#eb8334", fg="#fff",
                    width=18, height=2).place(bordermode=OUTSIDE, x=620, y=28)

func_fr7 = Button(fr7, text=" Área funcionario ", bg="#eb8334", fg="#fff",
                   width=18, height=2).place(bordermode=OUTSIDE, x=760, y=28)

about1_fr7 = HTMLLabel(fr7, html="<h2 style ='color:#f5f5f5;font:Mongolian Baiti;'>Excluir Usúario</h2>",
                       background='#8a37cc').place(bordermode=OUTSIDE, x=450, y=150)

form_fr7 = HTMLLabel(fr7, html="<img src='fr6_fr7.png'>", width=112, height=27,
                     background='#8a37cc').place(bordermode=OUTSIDE, x=220, y=120)

cpf_user_fr7 = Entry(fr7, bg="#eb8334", width=17, font='Arial 25').place(
    bordermode=OUTSIDE, x=285, y=248)

passw_func__fr7 = Entry(fr7, bg="#eb8334", width=17, font='Arial 25').place(
    bordermode=OUTSIDE, x=285, y=362)

show_fr7 = Button(fr7, text='👁', font=('Mongolian Baiti', "18", "bold"), bg='#eb8334', fg='#fff').place(
    bordermode=OUTSIDE, x=605, y=360)

entra_fr7 = Button(fr7, text=" Excluir ", font=('Mongolian Baiti', '15'), bg="#eb8334",
                   fg="#fff", width=24, height=2).place(bordermode=OUTSIDE, x=300, y=455)


# falta criar tela de funcionalidade de usuario deposito saque transferencia e extrato
# falta criar tela de exclusão de usuario da linha do funcionario
# falta criar tela de criação de conta user pela linha do funcionario
# falta criar tela de troca de informações de usuario para ele mesmo

# No total falta a criação de 7 telas de funcionalidade fora troca de frames e funções

root.mainloop()
