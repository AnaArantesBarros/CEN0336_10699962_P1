#Importando pacotes necessários
import sys

#Puxando valores de input
a = sys.argv[1]
b = sys.argv[2]

#Verifica se os inputs são números
if a.replace("-","").isdigit() == False:
    print("O input a deve ser um número.")
if b.replace("-","").isdigit() == False:
    print("O input b deve ser um número.")


# Se os dois inputs são números
else:
    #Convertendo para formato integer/inteiro
    a = int(a)
    b = int(b)
    #Verifica se os inputs são maiores que zero
    if a <= 0 or b <= 0:
        # Se apenas b for menor ou igual a zero
        if b <= 0 and a>= 0:
            print("O valor b não é um número positivo e maior que zero, tente novamente.")
        # Se apenas a for menor ou igual a zero
        if a <= 0 and b>=0:
            print("O valor a não é um número positivo e maior que zero, tente novamente.")
        # Se a e b são menores ou iguais a zero
        elif a <= 0 and a <= 0:
            print("Nenhum dos valores fornecidos é positivo e maior que zero, tente novamente.")

    #Verifica se os valores são positivos
    if a>0 and b>0:
        # Se os inputs são menores que 500
        if a < 500 and b < 500:
            A = (a * b) / 2
            print(f'A área do triangulo retângulo com lados a={a} e b={b}, é de {A}')
        # Se algum dos inputs forem maiores ou iguais a 500
        elif a >= 500 or b >= 500:
            print("Os valores fornecidos precisam ser menores que 500.")
