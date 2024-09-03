# Escreva um programa que inverta os caracteres de um string.
#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;


def inverter_string(s):
    # Usando slicing para inverter a string
    return s[::-1]

# Solicitar uma string ao usuário
string_original = input("Digite uma string para inverter: ")

# Chamar a função e exibir a string invertida
string_invertida = inverter_string(string_original)
print(f"A string invertida é: {string_invertida}")
