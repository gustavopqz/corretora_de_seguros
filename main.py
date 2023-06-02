import mysql.connector
from tkinter import *
from tkinter import messagebox
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv("USER")
password = os.getenv("PASSWORD")

def inserir_dados():
    conexao = mysql.connector.connect(
        host="localhost",
        user=user,
        password=password,
        database="corretora"
    )
    cursor = conexao.cursor()

    # Coletando dados
    nome = nome_func.get()
    cpf = cpf_func.get()
    telefone = tel_func.get()
    rua = rua_func.get()
    cidade = cidade_func.get()
    estado = estado_func.get()
    pais = pais_func.get()
    cep = cep_func.get()

    # Gerando insert
    query = "INSERT INTO funcionario (nome, cpf, telefone, rua, cidade, estado, pais, cep) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    valores = (nome.upper(), cpf, telefone, rua.upper(), cidade.upper(), estado.upper(), pais.upper(), cep)

    # Executando e fexando conexão após insert
    cursor.execute(query, valores)
    conexao.commit()
    cursor.close()
    conexao.close()
    confirmInsert()
    
    # Retirando os valores para novos cadastros
    nome_func.delete(0, END)
    cpf_func.delete(0, END)
    tel_func.delete(0, END)
    rua_func.delete(0, END)
    cidade_func.delete(0, END)
    estado_func.delete(0, END)
    pais_func.delete(0, END)
    cep_func.delete(0, END)

# Instanciando o Tkinter
janela = Tk()
janela.title("Cadastro de Funcionários")
janela.geometry("900x600")
janela.configure(background="#dde")

# Imagem background
imagem = PhotoImage(file="./background.png")

label_imagem = Label(janela, image=imagem)
label_imagem.pack()

# Inputs
Label(janela, text="Nome", background="#fff", foreground="#009", anchor=N).place(x=400, y=10, width=100, height=20)
nome_func=Entry(janela)
nome_func.place(x=350, y=30, width=200, height=20)


Label(janela, text="CPF", background="#fff", foreground="#009", anchor=N).place(x=400, y=110, width=100, height=20)
cpf_func=Entry(janela)
cpf_func.place(x=350, y=130, width=200, height=20)


Label(janela, text="Telefone", background="#fff", foreground="#009", anchor=N).place(x=400, y=60, width=100, height=20)
tel_func=Entry(janela)
tel_func.place(x=350, y=80, width=200, height=20)


Label(janela, text="Rua", background="#fff", foreground="#009", anchor=N).place(x=400, y=160, width=100, height=20)
rua_func=Entry(janela)
rua_func.place(x=350, y=180, width=200, height=20)


Label(janela, text="Cidade", background="#fff", foreground="#009", anchor=N).place(x=400, y=210, width=100, height=20)
cidade_func=Entry(janela)
cidade_func.place(x=350, y=230, width=200, height=20)


Label(janela, text="Estado", background="#fff", foreground="#009", anchor=N).place(x=400, y=260, width=100, height=20)
estado_func=Entry(janela)
estado_func.place(x=350, y=280, width=200, height=20)


Label(janela, text="País", background="#fff", foreground="#009", anchor=N).place(x=400, y=310, width=100, height=20)
pais_func=Entry(janela)
pais_func.place(x=350, y=330, width=200, height=20)


Label(janela, text="CEP", background="#fff", foreground="#009", anchor=N).place(x=400, y=360, width=100, height=20)
cep_func=Entry(janela)
cep_func.place(x=350, y=380, width=200, height=20)


# Botão
btn_cadastro=Button(janela, text="Cadastrar", command=inserir_dados).place(x=400, y=430, width=100, height=20)

# Janela de confirmação
def confirmInsert():
    nome = nome_func.get()
    mensagem = f"Usuário {nome} cadastrado com sucesso!"
    messagebox.showinfo("Sucesso", mensagem)

# Manter janela aberta
janela.mainloop()