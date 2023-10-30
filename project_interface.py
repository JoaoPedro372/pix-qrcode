import random
import string
from PIL import Image, ImageTk
from random import choice
import tkinter as tk


def generate_password(length, uppercase=False, digits=False, punctuation=False):
    # Cria uma string com todos os caracteres que podem ser usados na senha
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if punctuation:
        characters += string.punctuation

    # Verifica se foram selecionados requisitos mínimos suficientes
    if len(characters) < length:
        raise ValueError(
            "Requisitos mínimos selecionados não são suficientes para gerar uma senha com o comprimento desejado")

    # Gera uma senha aleatória de acordo com o comprimento especificado
    password = ''.join(random.choice(characters) for i in range(length))

    return password


def generate_and_show_password():
    # Obter parâmetros para gerar a senha
    password_length = int(length_entry.get())
    uppercase = uppercase_var.get()
    digits = digits_var.get()
    punctuation = punctuation_var.get()

    # Gerar senha e exibi-la na tela
    try:
        password = generate_password(
            password_length, uppercase, digits, punctuation)
        password_label.config(text=password)
    except ValueError as e:
        password_label.config(text="Erro: " + str(e))

# Criar janela principal
root = tk.Tk()
root.geometry("500x500")
root.minsize(500, 500) 
root.maxsize(500, 500)
root.title("Gerador de Senhas")

# Criar entrada de texto para o comprimento da senha
length_label = tk.Label(root, text="Comprimento da senha:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack(pady=10)

# Criar checkbox para caracteres maiúsculos
uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(
    root, text="Letras Maiúsculas", variable=uppercase_var)
uppercase_checkbox.pack(pady=10)

# Criar checkbox para dígitos
digits_var = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(root, text="Dígitos", variable=digits_var)
digits_checkbox.pack(pady=10)

# Criar checkbox para caracteres de pontuação
punctuation_var = tk.BooleanVar()
punctuation_checkbox = tk.Checkbutton(
    root, text="Caracteres de Pontuação", variable=punctuation_var)
punctuation_checkbox.pack(pady=10)

# Criar botão para gerar a senha
generate_button = tk.Button(
    root, text="Gerar Senha", command=generate_and_show_password)
generate_button.pack(pady=10)

# Criar label para exibir a senha gerada
password_label = tk.Label(root, text="")
password_label.pack(pady=10)

# Criar label para exibir o QRCode da senha gerada
qr_label = tk.Label(root)
qr_label.pack()

# Iniciar a janela principal
root.mainloop()