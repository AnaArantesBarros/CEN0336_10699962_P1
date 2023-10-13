import sys

# Recebendo inputs do usuário
dna = sys.argv[1]
n1 = sys.argv[2]
n2 = sys.argv[3]
n3 = sys.argv[4]
n4 = sys.argv[5]
n5 = sys.argv[6]
n6 = sys.argv[7]

# Verificando se o formato dos dados estão corretos
lista = [n1,n2,n3,n4,n5,n6]
for i in lista:
    if str(i).isdigit() == False:
        # Se a string conter '-' pode ser um número negativo
        if '-' in i:
                # Se for um número negativo informar ao usuário
                if str(i).replace('-','').isdigit() == True:
                    print(f'O valor de n{lista.index(i)+1} deve ser um número positivo.')
                    sys.exit(1) #Para de executar o código
        # Se só for uma string informar o usuário
        else:
            print(f'O valor de n{lista.index(i)+1} deve ser um número.')
            sys.exit(1) #Para de executar o código
    # Se todos forem digitos então covertemos seu formato para inteiro/integer
    else:
        n1,n2,n3,n4,n5,n6 = int(n1),int(n2),int(n3),int(n4),int(n5),int(n6)
        # Verifica se o tamanho é menor que o comprimento do dna
        if int(i) > len(dna):
            print(f'o valor de n{lista.index(i) + 1} deve ser menor que o tamanho do dna ({len(dna)})')
            sys.exit(1)  # Para de executar o código


if dna.isdigit() == True:
    print('O dna passado deve ser uma string.')
    sys.exit(1)

# Extraindo sequências CDS
CDS1 = dna[n1-1:n2]
CDS2 = dna[n3-1:n4]
CDS3 = dna[n5-1:n6]

# Verifica se as sequências alvos estão em CDS1 e CDS3
CDS1_status = 'ATG' in CDS1git
CDS3_status =  'TAG' in CDS3 or 'TAA' in CDS3 or 'TGA' in CDS3
join_status = CDS1_status == True and CDS3_status == True

# Se as sequências estão em CDS1 e CDS3 concatena
if join_status == True:
    print(CDS1+CDS2+CDS3)