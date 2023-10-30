import random
import string
import qrcode


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


# Pergunta ao usuário o comprimento desejado para a senha
password_length = int(input("Digite o comprimento desejado para a senha: "))

# Pergunta ao usuário se a senha deve conter letras maiúsculas
uppercase = input(
    "A senha deve conter letras maiúsculas? (sim/não) ").lower() == "sim"

# Pergunta ao usuário se a senha deve conter dígitos
digits = input("A senha deve conter dígitos? (sim/não) ").lower() == "sim"

# Pergunta ao usuário se a senha deve conter caracteres de pontuação
punctuation = input(
    "A senha deve conter caracteres de pontuação? (sim/não) ").lower() == "sim"

# Gera e imprime a senha aleatória de acordo com os requisitos selecionados
try:
    password = generate_password(
        password_length, uppercase, digits, punctuation)
    print("A senha gerada é:", password)
except ValueError as e:
    print("Erro:", e)



























# imagem = qrcode.make(password)
# imagem.save("senha.png")
