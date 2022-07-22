
# Pedir dois números e imprimir o maior
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

if num1 > num2:
    print("O maior número é: ",num1)
elif num1 < num2:
    print("O maior número é: ",num2)
else:
    print("Ambos os números são iguais a ",num1)



# Pedir valor e mostrar na tela se é positivo ou negativo
valor = float(input("Digite um número qualquer: "))

if valor < 0:
    print(valor, " é um número negativo.")
elif valor > 0:
    print(valor, " é um número positivo.")
else:
    print(valor, " é igual a zero, ou seja, não é positivo nem negativo")



# Digitar o sexo de uma pessoa
sexo = input("Digite M para sexo masculino ou F para sexo Feminino: ")

if sexo == "M" or sexo == "m":
    print("MASCULINO")
elif sexo == "F" or sexo == "f":
    print("FEMININO")
else:
    print("Sexo Inválido")



# Vogal ou Consoante?
letra = input("Digite uma letra qualquer: ")
letra = letra.upper()
vogal = ["A", "E", "I", "O", "U"]
consoante = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S","T", "V", "W", "X", "Y", "Z"]

i = 0
while i < len(vogal):
    if letra == vogal[i]:
        print("A letra é uma vogal")
        i = len(vogal)+1
    else:
        i+=1
j = 0
while j < len(consoante):
    if letra == consoante[j]:
        print("A letra é uma consoante")
        j = len(consoante)+1
    else:
        j+=1

if i == len(vogal) and j == len(consoante):
    print("Você deve ter digitado incorretamente")




# Ler duas notas parciais de um aluno, calcular média e retornar status
np1 = float(input("Digite a primeira nota parcial do aluno: "))
np2 = float(input("Digite a segunda nota parcial do aluno: "))
media = (np1+np2)

if media == 10:
    print("Aluno aprovado com distinção.")
elif media >= 7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado.")



# Ler três números e mostrar o menor deles
num1 = float(input("Digite um número qualquer: "))
num2 = float(input("Digite outro número: "))
num3 = float(input("Digite mais um número: "))

if num1>num2:
    if num1>num3:
        print("O maior número é: ", num1)
        if num2>num3:
            print("O menor número é: ", num3)
        else:
            print("O menor número é: ", num2)
    else:
            print("O maior número é: ", num3)
            print("O menor número é: ", num2)

else:
    if num2>num3:
        print("O maior número é: ", num2)
        if num1>num3:
            print("O menor número é: ", num3)
        else:
            print("O menor número é: ", num1)
    else:
            print("O maior número é: ", num3)
            print("O menor número é: ", num1)




# Perguntar o preço de três produtos e indicar qual comprar (o mais barato)
prod1 = float(input("Digite o valor do produto X: "))
prod2 = float(input("Digite o valor do produto Y: "))
prod3 = float(input("Digite o valor do produto Z: "))

if prod1<prod2:
    if prod1<prod3:
        print("Compre o produto X!")
    else:
        print("Compre o produto Z!")
else:
    if prod2<prod3:
        print("Compre o produto Y!")
    else:
        print("Compre o produto Z!")




# Ler três números e mostrá-los em ordem decrescente
x = float(input("Digite um número qualquer: "))
y = float(input("Digite outro número: "))
z = float(input("Digite mais um número: "))

if x>y:
    if x>z:
        if y>z:
            print("A ordem decrescente é: ", x,", ", y,", ", z)
        else:
            print("Os números em ordem decrescente são: ", x,", ", z,", ", y)
    else:
        print("Os números em ordem decrescente são: ", z,", ", x,", ", y)
else:
    if y>z:
        if x>z:
            print("Os números em ordem decrescente são: ", y,", ", x,", ", z)
        else:
            print("Os números em ordem decrescente são: ", y,", ", z,", ", x)
    else:
        print("Os números em ordem decrescente são: ", z,", ", y,", ", x)




# Perguntar em que turno você estuda
turno = input("Digite a letra inicial do turno em que você estuda (Manhã - M; Tarde - T; Noite - N): ")
turno = turno.upper()

if turno == "M":
    print("Bom dia!")
elif turno == "T":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor digitado não é válido.")



# Aumento de salário TABAJARA
salario = float(input("Digite o valor do salário bruto a sofrer reajuste: "))
print("O salário antes do reajuste era de: R$ ", salario)

if salario <= 280:
    novoSalario = salario * 1.2
    print("O percentual de aumento aplicado foi de 20%.")
elif salario >280 and salario <=700:
    novoSalario = salario * 1.15
    print("O percentual de aumento aplicado foi de 15%.")
elif salario >700 and salario <=1500:
    novoSalario = salario * 1.10
    print("O percentual de aumento aplicado foi de 10%.")
else:
    novoSalario = salario * 1.05
    print("O percentual de aumento aplicado foi de 5%.")

print("O valor do aumento dado é de: R$", novoSalario-salario)
print("O salário reajustado é: R$ ", novoSalario)




# Folha de Pagamento
valorHora = float(input("Qual é o valor de sua hora trabalhada? "))
horas = float(input("Quantas horas você trabalhou neste mês: "))
salarioBruto = valorHora * horas

if salarioBruto <= 900:
    descontoIR = 0
elif salarioBruto <= 1500:
    descontoIR = salarioBruto * 0.05
elif salarioBruto <= 2500:
    descontoIR = salarioBruto * 0.10
else:
    descontoIR = salarioBruto * 0.20

descontoSindicato = salarioBruto * 0.03
depositoFGTS = salarioBruto * 0.11

salarioLiq = salarioBruto - descontoIR - descontoSindicato

print("Salário Bruto:--- R$", salarioBruto)
print("Descontos: ")
print("Sindicato: -------R$", descontoSindicato)
print("Imposto de Renda: R$", descontoIR)
print("Salário Líquido: -R$", salarioLiq)
print("-----------------------------------")
print("Depósito FGTS: ---R$", depositoFGTS)



# Dia da Semana
num = int(input("Digite um número de 1 a 7 para obter o dia da semana correspondente: "))
dia_da_semana = {1:"Domingo", 2:"Segunda-Feira", 3:"Terça-Feira", 4:"Quarta-Feira", 5:"Quinta-Feira", 6:"Sexta-Feira", 7:"Sábado"}

if num < 1 or num > 7:
    print("Você digitou um número inválido.")
else:
    print("O dia da semana correspondente é: ", dia_da_semana[num])



# Ler duas notas parciais de um aluno e retornar a média
np1 = float(input("Digite a primeira nota parcial do aluno: "))
np2 = float(input("Digite a segunda nota parcial do aluno: "))

media = (np1 + np2)/2

if media >= 9:
    conceito = "A"
elif media >= 7.5 and media < 9:
    conceito = "B"
elif media >= 6 and media < 7.5:
    conceito = "C"
elif media >= 4 and media < 6:
    conceito = "D"
else:
    conceito = "E"

if conceito == "A" or conceito == "B" or conceito == "C":
    resultado = "ALUNO APROVADO"
else:
    resultado = "ALUNO REPROVADO"

print("----Notas: "+str(np1)+", "+str(np2))
print("----Média: "+str(media))
print("-Conceito: "+conceito)
print("Resultado: "+resultado)



# Pedir os três lados de um triângulo
lados = []
for i in range(3):
    lados.append(float(input("Digite o tamanho do lado "+str(i+1)+" do triângulo: ")))

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



# Raízes de uma equação do segundo grau do tipo ax² + bx + c = 0
a = float(input("Digite o valor do coeficiente quadrático a: "))
b = float(input("Digite o valor do coeficiente linear b: "))
c = float(input("Digite o valor do coeficiente constante c: "))

d = ((b**2)-(4*a*c))
delta = (d)**(1/2)
if d < 0:
    print("A equação não possui raízes reais")
elif delta == 0:
    x = -b / (2*a)
    print("A equação possui uma raiz, cujo valor é: ", x)
else:
    x1 = (-b + delta)/(2*a)
    x2 = (-b - delta)/(2*a)
    print("A equação possui duas raízez, cujos valores são: ", x1, " e ", x2)



# Informar se o ano é ou não bissexto
ano = int(input("Digite um ano: "))

if ano%400 == 0:
    print("É ano bissexto")
elif ano%4 == 0 and ano%100 !=0:
    print("É ano bissexto")
else:
    print("Não é ano bissexto")



# Pedir data em formato dd/mm/aaaa e verificar se é uma data válida
data = input("digite uma data no formato dd/mm/aaaa: ")
listaData = data.split("/")

if len(listaData[0]) == 2 and len(listaData[1]) == 2 and len(listaData[2]) == 4:
    if int(listaData[0]) > 0 and int(listaData[0]) < 32:
        if int(listaData[1]) > 0 and int(listaData[1]) < 13:
            if int(listaData[2]) > 0:
                print("A data digitada é válida.")
            else:
                print("A data é inválida. Encontrado erro no ano")
        else:
            print("A data é inválida. Encontrado erro no mês")
    else:
        print("A data é inválida. Encontrado erro no dia")
else:
    print("A data é inválida. Número de caracteres não bate com o formato requerido.")



# Ler número inteiro menor que 1000 e contar centenas, dezenas e unidades (respondi de dois modos, pois não sei se entendi direito o enunciado)
numero = int(input("Digite um número inteiro menor que 1000:"))

if numero < 1000:
    centenas = int(numero/100)
    dezenas = int((numero - 100*centenas)/10)
    unidades = numero - 100*centenas - 10*dezenas
else:
    print("Você digitou número inválido")

#resposta 1
print("O número é composto por: ",centenas, " centenas +", dezenas, " dezenas  +", unidades, " unidades")
#resposta2
print("O número possui: ", int(numero/100), " centenas inteiras")
print("O número possui: ", int(numero/10), " dezenas inteiras")
print("O número possui ", numero, " unidades inteiras")
