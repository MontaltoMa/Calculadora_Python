from tkinter import *

janela = Tk()
janela.title ('Calculadora')
janela.geometry('408x355')
janela.minsize(408,355)
janela.maxsize(408,355)
janela.configure(background='#282828')

#Variáveis globais
numero1 = ''
divisao = False
multiplicacao = False
subtracao = False
soma = False

#Campo de entrada
e = Entry(janela, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF', bg='#a7a28f', font=('futura', 25, 'bold'),justify=CENTER)
e.grid(row=0, column=0, columnspan=3, pady=2)

# Funções
def botao_click(num):
    e.insert(END, num)

def botao_limpar():
    e.delete(0, END)

def botao_igual():
    global numero1
    global divisao
    global multiplicacao
    global subtracao
    global soma

    numero2 = e.get()
    e.delete(0, END)

    if divisao:
        try:
            resultado = float(numero1) / float(numero2)
        except ZeroDivisionError:
            resultado = "Erro"
        e.insert(0, str(resultado))
        divisao = False
    elif multiplicacao:
        resultado = float(numero1) * float(numero2)
        e.insert(0, str(resultado))
        multiplicacao = False
    elif subtracao:
        resultado = float(numero1) - float(numero2)
        e.insert(0, str(resultado))
        subtracao = False
    elif soma:
        resultado = float(numero1) + float(numero2)
        e.insert(0, str(resultado))
        soma = False

def botao_divisao():
    global numero1
    global divisao
    divisao = True
    numero1 = e.get()
    e.delete(0, END)

def botao_multiplicacao():
    global numero1
    global multiplicacao
    multiplicacao = True
    numero1 = e.get()
    e.delete(0, END)

def botao_subtracao():
    global numero1
    global subtracao
    subtracao = True
    numero1 = e.get()
    e.delete(0, END)

def botao_soma():
    global numero1
    global soma
    soma = True
    numero1 = e.get()
    e.delete(0, END)


#Primeira linha
divisao = Button(janela, text='/', padx=42.5, pady=20, command=botao_divisao, fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold')).grid(row=1,column=3)

um = Button(janela, text='1', padx=40, pady=20, command=lambda: botao_click(1), fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold')).grid(row=3,column=0)

dois = Button(janela, text='2', padx=40, pady=20, command=lambda: botao_click(2), fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold')).grid(row=3,column=1)

tres = Button(janela, text='3', padx= 40, pady=20, command=lambda: botao_click(3), fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold')).grid(row=3,column=2)

multiplicacao = Button(janela, text='x', padx=40, pady=20, command=botao_multiplicacao, fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold')).grid(row=2,column=3)


#Segunda linha
quatro = Button(janela, text='4', padx=40, pady=20, command=lambda: botao_click(4), fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold')).grid(row=2,column=0)

cinco = Button(janela, text='5', padx=40, pady=20, command=lambda: botao_click(5), fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold')).grid(row=2,column=1)

seis = Button(janela, text='6', padx=40, pady=20, command=lambda: botao_click(6), fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold')).grid(row=2,column=2)

subtracao = Button(janela, text='-', padx=41.5, pady=20, command=botao_subtracao, fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold')).grid(row=3,column=3)


#Terceira linha
sete = Button(janela, text='7', padx=40, pady=20, command=lambda: botao_click(7), fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold')).grid(row=1,column=0)

oito = Button(janela, text='8', padx=40, pady=20, command=lambda: botao_click(8), fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold')).grid(row=1,column=1)

nove = Button(janela, text='9', padx=40, pady=20, command=lambda: botao_click(9), fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold')).grid(row=1,column=2)

soma = Button(janela, text='+', padx=40, pady=20, command=botao_soma, fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold')).grid(row=4,column=3)


#Quarta linha
zero = Button(janela, text='0', padx=40, pady=20, command=lambda: botao_click(0), fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold')).grid(row=4,column=0)

ponto = Button(janela, text='.', padx=42, pady=20, command=lambda: botao_click('.'), fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold')).grid(row=4,column=1)

enter = Button(janela, text='=', padx=40, pady=20, command=botao_igual, fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold')).grid(row=4,column=2)

#Limpar
limpar = Button(janela, text='C', padx=40, pady=20, command= botao_limpar, fg='#ffffff', activeforeground='#ffffff', bg='#320064', activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold')).grid(row=0,column=3)
janela.mainloop()