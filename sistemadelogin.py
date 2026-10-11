print('SISTEMA DE LOGIN')

senha_correta = "admin"
usuario_correto = "admin"

senha = input("Digite a senha: ")
usuario = input("Digite o usuário: ")

if senha == senha_correta and usuario == usuario_correto:
    print("Login bem-sucedido!")
else:
    print("Senha ou usuário incorretos. Tente novamente.")


#banco = sqlite3.connect('projeto_banco.db')
#cursor = banco.cursor()
#cursor.execute("CREATE TABLE IF NOT EXISTS registro (nome text, email text, senha text)")
#banco.commit()
#banco.close()

def clique(email, senha):
    email_usuario = email.get()
    senha_usuario = senha.get()

    print("Fazer Login")

botao = customtkinter.CTkButton(janela, text="Login", command=lambda: clique(email, senha))
botao.pack(padx=10, pady=10)