import customtkinter
import sqlite3

banco = sqlite3.connect('projeto_banco.db')



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def clique2():
    from telacadastro import abrir_cadastro
    abrir_cadastro(janela)

def clique():
    email_digitado = email.get()
    senha_digitada = senha.get()

    banco = sqlite3.connect("projeto_banco.db")
    cursor = banco.cursor()

    cursor.execute("""
        SELECT nome
        FROM registro
        WHERE email = ? AND senha = ?
    """, (email_digitado, senha_digitada))

    usuario = cursor.fetchone()

    if usuario:
        from telaentrada import abrir_entrada
        abrir_entrada(janela)
        print("Login realizado!")
    else:
        print("E-mail ou senha incorretos.")

    banco.close()
    
janela = customtkinter.CTk()
janela.geometry("840x500")
texto = customtkinter.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text="Seu e-mail")
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
senha.pack(padx=10, pady=10)

check = customtkinter.CTkCheckBox(janela, text="Lembrar Login")
check.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)

botao2 = customtkinter.CTkButton(janela, text="Cadastrar", command=clique2)
botao2.pack(padx=10, pady=10)

janela.mainloop()