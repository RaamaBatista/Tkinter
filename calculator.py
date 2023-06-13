from tkinter import * #importando o tkinter#

janela= Tk()#criando a janela
janela.title('TKINTER- CALCULADORA')#titulo da janela
janela.geometry('445x530')#Ajustar tamanho da janela, sendo o primeiro valor a largura e depois a altura 
janela.config(bg='white')#alterar cor do fundo da janela

numero1= ''
mais= FALSE
divisao= FALSE
multiplica= FALSE
menos=FALSE


entrada= Entry(janela,width=15,borderwidth=4, relief='flat',fg='#FFFFFF',bg='#a7a28f', font=('futura',25,'bold'), justify=CENTER )#criando o input, relief é o relevo
entrada.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)
#funções 

def bclick(num):
    entrada.insert(END,num) #colocando argumento no input
    
def bdivisao():
    global numero1
    global divisao
    divisao=TRUE
    numero1= entrada.get()#pegar o numerom clicado
    entrada.delete(0,END)#limpar input após apertar o botão de dividir

def bmultiplica():
    global numero1
    global multiplica
    multiplica=TRUE
    numero1= entrada.get()#pegar o numerom clicado
    entrada.delete(0,END)#limpar input após apertar o botão de dividir
def bmenos():
    global numero1
    global menos
    menos=TRUE
    numero1= entrada.get()#pegar o numerom clicado
    entrada.delete(0,END)#limpar input após apertar o botão de dividir
def bmais():
    global numero1
    global mais
    mais=TRUE
    numero1= entrada.get()#pegar o numerom clicado
    entrada.delete(0,END)#limpar input após apertar o botão de dividir

def bigual():
   global divisao
   global menos
   global mais
   global multiplica
   numero2= entrada.get()
   entrada.delete(0, END)

   if mais==TRUE:
       entrada.insert(0, int(numero1)+int(numero2))
       mais=FALSE

   if menos==True:
       entrada.insert(0, int(numero1)-int(numero2))
       menos=FALSE
   if multiplica==True:
       entrada.insert(0, int(numero1)*int(numero2))
       multiplica=FALSE
   if divisao==True:
       entrada.insert(0, int(numero1)/int(numero2))
       divisao=FALSE

def blimpa():
    entrada.delete(0, END)
divisao= Button(janela,
                text='÷',
                padx=40,
                pady=20,
                height=2,
                command=bdivisao,
                fg='#000000',
                activebackground='#240046',
                bg='#FF0000',
                relief=FLAT,
                font=('Arial', 16),
                )
divisao.grid(
    row=0,
    column=4
)

multiplica= Button(janela,
                text='*',
                padx=42,
                pady=20,
                height=2,
                command=bmultiplica,
                fg='#000000',
                activebackground='#240046',
                bg='#FF0000',
                relief=FLAT,
                font=('Arial', 16),
                )
multiplica.grid(
    row=1,
    column=4
)
menos= Button(janela,
                text='-',
                padx=43,
                pady=20,
                height=2,
                command=bmenos,
                fg='#000000',
                activebackground='#240046',
                bg='#FF0000',
                relief=FLAT,
                font=('Arial', 16),
                )
menos.grid(
    row=2,
    column=4
)

adicao= Button(janela,
                text='+',
                padx=41,
                pady=20,
                height=2,
                command=bmais,
                fg='#000000',
                activebackground='#240046',
                bg='#FF0000',
                relief=FLAT,
                font=('Arial', 16),
                )
adicao.grid(
    row=3,
    column=4
)

um= Button(janela,
                text='1',
                padx=40,
                pady=20,
                height=2,
                command=lambda:bclick(1),
                fg='#000000',
                activebackground='#240046',#quando clicar mud de cor
                bg= '#F7FDA7',
                relief=FLAT,
                font=('Arial', 16),
                )

  
um.grid(
    row=1,
    column=1
)

dois= Button(janela,
                text='2',
                padx=40,
                pady=20,
                height=2,
                command=lambda:bclick(2),
                fg='#000000',
                activebackground='#240046',#quando clicar mud de cor
                bg= '#F7FDA7',
                relief=FLAT,
                font=('Arial', 16),
                )
dois.grid(
    row=1,
    column=2
)

tres= Button(janela,
                text='3',
                padx=41,
                pady=20,
                height=2,
                command=lambda:bclick(3),
                fg='#000000',
                activebackground='#240046',#quando clicar mud de cor
                bg= '#F7FDA7',
                relief=FLAT,
                font=('Arial', 16),
                )
tres.grid(
    row=1,
    column=3
)

quatro= Button(janela,
                text='4',
                padx=41,
                pady=20,
                height=2,
                command=lambda:bclick(4),
                fg='#000000',
                activebackground='#240046',#quando clicar mud de cor
                bg= '#F7FDA7',
                relief=FLAT,
                font=('Arial', 16),
           
                )
quatro.grid(
    row=2,
    column=1
)

cinco= Button(janela,
                text='5',
                padx=41,
                pady=20,
                height=2,
                command=lambda:bclick(5),
                 fg='#000000',
                activebackground='#240046',#quando clicar mud de cor
                bg= '#F7FDA7',
                relief=FLAT,
                font=('Arial', 16),
               
                )
cinco.grid(
    row=2,
    column=2
)

seis= Button(janela,
                text='6',
                padx=40,
                pady=20,
                height=2,
                command=lambda:bclick(6),
                fg='#000000',
                activebackground='#240046',#quando clicar mud de cor
                bg= '#F7FDA7',
                relief=FLAT,
                font=('Arial', 16),
              
                )
seis.grid(
    row=2,
    column=3
)

sete= Button(janela,
                text='7',
                padx=40,
                pady=20,
                height=2,
                command=lambda:bclick(7),
                fg='#000000',
                activebackground='#240046',#quando clicar mud de cor
                bg= '#F7FDA7',
                relief=FLAT,
                font=('Arial', 16),
                )
sete.grid(
    row=3,
    column=1
)
oito= Button(janela,
                text='8',
                padx=40,
                pady=20,
                height=2,
                command=lambda:bclick(8),
                fg='#000000',
                activebackground='#240046',#quando clicar mud de cor
                bg= '#F7FDA7',
                relief=FLAT,
                font=('Arial', 16),
                )
oito.grid(
    row=3,
    column=2
)
nove= Button(janela,
                text='9',
                padx=40,
                pady=20,
                height=2,
                command=lambda:bclick(9),
                fg='#000000',
                activebackground='#240046',#quando clicar mud de cor
                bg= '#F7FDA7',
                relief=FLAT,
                font=('Arial', 16),
                )
nove.grid(
    row=3,
    column=3
)
#zero
zero= Button(janela,
                text='0',
                padx=91,
                pady=20,
                height=2,
                command=lambda:bclick(0),
                fg='#000000',
                activebackground='#240046',#quando clicar mud de cor
                bg= '#F7FDA7',
                relief=FLAT,
                font=('Arial', 16),
                )
zero.grid(
    row=4,
    column=1,
    columnspan=2
)

limpa= Button(janela,
                text='C',
                padx=39,
                pady=20,
                height=2,
                command=blimpa,
                fg='#000000',
                activebackground='#240046',
                bg='#228B22',
                relief=FLAT,
                font=('Arial', 16),
                )
limpa.grid(
    row=4,
    column=3
)

igual= Button(janela,
                text='=',
                padx=41,
                pady=20,
                height=2,
                command=bigual,
                fg='#000000',
                activebackground='#240046',
                bg='#FF6347',
                relief=FLAT,
                font=('Arial', 16),
                )
igual.grid(
    row=4,
    column=4
)


janela.mainloop()#para abir a janela do tkinter