import customtkinter
import sqlite3



def botao_cadastrar(nome, email, senha):
    nome_usuario = nome.get()
    email_usuario = email.get()
    senha_usuario = senha.get()

    


    banco = sqlite3.connect('projeto_banco.db')
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS registro (nome text, email text, senha text)")
    cursor.execute("""
        INSERT INTO registro (nome, email, senha)
        VALUES (?, ?, ?)
    """, (nome_usuario, email_usuario, senha_usuario))

    banco.commit()
    banco.close()


    print("Usuário cadastrado com sucesso!")



def abrir_cadastro(janela_principal=None):
    janela_cadastro = customtkinter.CTkToplevel(janela_principal)

    janela_cadastro.title("Cadastro")
    janela_cadastro.geometry("500x400")

    titulo = customtkinter.CTkLabel(
        janela_cadastro,
        text="Criar uma conta",
        font=("Arial", 20)
    )
    titulo.pack(padx=10, pady=20)

    nome = customtkinter.CTkEntry(
        janela_cadastro,
        placeholder_text="Seu nome"
    )
    nome.pack(padx=10, pady=10)

    email = customtkinter.CTkEntry(
        janela_cadastro,
        placeholder_text="Seu e-mail"
    )
    email.pack(padx=10, pady=10)

    senha = customtkinter.CTkEntry(
        janela_cadastro,
        placeholder_text="Sua senha",
        show="*"
    )
    senha.pack(padx=10, pady=10)

    confirmar_senha = customtkinter.CTkEntry(
        janela_cadastro,
        placeholder_text="Confirme sua senha",
        show="*"
    )
    confirmar_senha.pack(padx=10, pady=10)
    if senha.get() != confirmar_senha.get():
        print("As senhas não coincidem!")
        return

    botao_cadastro = customtkinter.CTkButton(janela_cadastro, text="Cadastrar-se", command=lambda: botao_cadastrar(nome, email, senha))
    botao_cadastro.pack(padx=10, pady=20)

    # Coloca a janela de cadastro na frente da janela principal
    janela_cadastro.transient(janela_principal)
    janela_cadastro.grab_set()