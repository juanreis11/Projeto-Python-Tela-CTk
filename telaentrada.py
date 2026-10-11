import customtkinter
import sqlite3



def botao_entrar():
    print("Usuário entrou com Sucesso!")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


def abrir_entrada(janela_principal=None):
    janela_entrada = customtkinter.CTkToplevel(janela_principal)

    janela_entrada.title("Bem-vindo")
    janela_entrada.geometry("500x400")

    titulo = customtkinter.CTkLabel(
        janela_entrada,
        text="Pagina Inicial",
        font=("Arial", 20)
    )
    titulo.pack(padx=10, pady=20)

   

    botao_entrada = customtkinter.CTkButton(janela_entrada, text="Olá, Seja Bem-Vindo!", command=botao_entrar)
    botao_entrada.pack(padx=10, pady=20)

    # Coloca a janela de cadastro na frente da janela principal
    janela_entrada.transient(janela_principal)
    janela_entrada.grab_set()


