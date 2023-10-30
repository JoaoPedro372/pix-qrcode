import random
import string
import qrcode
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

    #Define tamanho do QrCode
    box_size = 7

    # Gerar o QRCode da senha e exibi-la na tela
    imagem = qrcode.make(password, box_size=box_size)
    imagem.save("senha.png")
    qr_image = Image.open("senha.png")
    qr_photo = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo

# Criar janela principal
root = tk.Tk()
root.geometry("600x600")
root.minsize(600, 600) 
root.maxsize(600, 600)
root.title("Gerador de Senhas")


# Criar entrada de texto para o comprimento da senha
length_label = tk.Label(root, text="Comprimento da senha:")
length_label.pack(pady=10)
length_entry = tk.Entry(root)
length_entry.pack()

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

# Criar botão para gerar a senha e o QRCode
generate_button = tk.Button(
    root, text="Gerar Senha", command=generate_and_show_password)
generate_button.pack(pady=10)

# Criar label para exibir a senha gerada
password_label = tk.Label(root, text="")
password_label.pack()

# Criar label para exibir o QRCode da senha gerada
qr_label = tk.Label(root)
qr_label.pack()

# Iniciar a janela principal
root.mainloop()