"""
#Salário Mês
p = "n"

while p == "n" or p == "N":
    salarioHora = float(input("Quanto você ganha por hora trabalhada? "))
    horasTrabalhadas = float(input("Qual foi o número de horas que você trabalhou no último mês? "))
    print("No último mês você trabalhou ", horasTrabalhadas, " horas, a um valor de R$ ", salarioHora, " por hora trabalhada.")
    p = input("Digite s para confirmar as informações ou n para digitá-las novamente: ")

salarioMes = salarioHora * horasTrabalhadas
print("Você faz jus a um salário de: R$ ", salarioMes, " referente ao último mês trabalhado.")


#Soma 2 números
soma = 0
for num in range(2):
    n = float(input("Digite o "+str(num+1)+"º número a ser somado: "))
    soma += n
else:
    print("O valor da soma dos dois números digitados é: ", soma)


#Quatro notas bimestrais -> Média
soma = 0
q = 4
for num in range(q):
    n = float(input("Digite a "+str(num+1)+"ª nota do aluno: "))
    soma += n
else:
    media = soma/q
    print("A média aritimétida do aluno é: ", media)


#Dois nº inteiros e um nº real (Calcule e mostre oq? Com certeza faltava algo no enunciado)
produto = 1
for num in range(2):
    n = int(input("Digite o "+str(num+1)+"º numero inteiro: "))
    produto *= n
else:
    n = float(input("Digite um número real: "))
    produto *= n
    print("O produto entre os dois números inteiros e o número real é: ", produto)


#Peça 2 numeros e mostre o maior
for num in range(2):
    n = float(input("Digite o "+str(num+1)+"º número: "))
    if num == 0:
        maior = n
    if n>maior:
        maior = n
else:
    print("O maior dos dois números digitados é: ", maior)


#Peça 3 numeros e mostre o maior
for num in range(3):
    n = float(input("Digite o "+str(num+1)+"º número: "))
    if num == 0:
        maior = n
    if n>maior:
        maior = n
else:
    print("O maior dos dois números digitados é: ", maior)


#Peça 3 números e mostre o maior e o menor
for num in range(3):
    n = float(input("Digite o "+str(num+1)+"º número: "))
    if num == 0:
        maior = n
        menor = n
    if n>maior:
        maior = n
    if n<menor:
        menor = n
else:
    print("O maior dos três números é ", maior, " e o menor é", menor)


#Receber três preços e optar pelo mais barato.
for num in range(3):
    n = float(input("Digite o preço do "+str(num+1)+"º produto: "))
    if num == 0:
        menor = n
    if n<menor:
        menor = n
else:
    print("O produto que deve ser adquirido é aquele que custa: R$", menor)


#Pedir os três lados de um triângulo e dizer se é Isósceles, Equilátero ou Escaleno
lados = []
for lado in range(3):
    lado = float(input("Digite o valor do "+str(lado+1)+"º lado: "))
    lados.append(lado)

if lados[0] + lados[1] > lados[2] and lados[0] + lados[2] > lados[1] and lados[2] + lados[1] > lados[0]:
    print("Estes lados PODEm formar um triângulo.")
    if lados[0] == lados[1] == lados[2]:
        print("O triângulo é EQUILÁTERO.")
    elif lados[0] != lados[1] != lados[2]:
        print("O triângulo é ESCALENO")
    else:
        print("O triângulo é ISÓSCELES")
else:
    print("Estes lados NÃO PODEM formar um triângulo")


#Pedir três números e mostrá-los em ordem decrescente
numeros =[]
i = 0
while i<3:
    num = float(input("Digite o "+str(i+1)+"º número: "))
    if len(numeros)==0:
        numeros.append(num)
    elif len(numeros)==1:
        if num < numeros[0]:
            numeros.append(num)
        else:
            numeros.insert(0, num)
    elif len(numeros)==2:
        if num < numeros[-1]:
            numeros.append(num)
        else:
            if num < numeros[-2]:
                numeros.insert(1, num)
            else:
                numeros.insert(0, num)
    i+=1

print("Os números, em ordem decrecente, são: ",numeros)
"""