lista = [n for n in range(1, 25, 4)]
print(lista)


# SOMA DE ITENS DE UMA LISTA
soma=0
for n in lista:
    soma = soma + n
print(soma)


# PRODUTO DE ITENS DE UMA LISTA
produto=1
for n in lista:
    produto = produto * n
print(produto)


# MAIOR VALOR DE UMA LISTA
#Opção 1
maior = max(lista)
print(maior)

#Opção 2
i=0
j=len(lista)-1
while i != j:
    if lista[i]>lista[j]:
        j-=1
    else:
        i+=1
maior = lista[i]
print(maior)


# MENOR VALOR DE UMA LISTA
#Opção 1
menor = min(lista)
print(menor)

#Opção 2
i=0
j=len(lista)-1
while i != j:
    if lista[i]<lista[j]:
        j-=1
    else:
        i+=1
menor = lista[i]
print(menor)


#CONTAR REPETIÇÕES DE UMA STRINT E REGISTRAR EM UM DICIONÁRIO
url = "https://www.google.com"
dicionario = {k: url.count(k) for k in url}
print(dicionario)


#CONTAR QUANTAS STRINGS, COM MAIS DE 2 CARACTERES, DE UMA LISTA,
#COMEÇAM E TERMINAM COM O MESMO CARACTER
string_list = ["Alca", "Bovespa", "DDD", "Embraer", "RR", "ONU", "007", "16/07/2001"]
#Opção 1
i=0
for string in string_list:
    if len(string) > 2 and string[0] == string[-1]:
        i+=1
print(i)

#Opção 2
nova_lista = [string for string in string_list if len(string)>2 if string[0]==string[-1]]
print(len(nova_lista))


#ORDENAR LISTA DE TUPLAS PELO ÚLTIMO ELEMENTO DA TUPLAO
lista_t = [(1, 5), (3, 8), (9, 3), (5, 1), (8, 2)]

for i in range(len(lista_t)):
    menor = i
    for j in range (i+1, len(lista_t)):
        if lista_t[menor][1] > lista_t[j][1]:
            menor = j
    lista_t[i], lista_t[menor] = lista_t[menor], lista_t[i]

print(lista_t)


#ADICIONAR UMA CHAVE(KEY), COM SEU RESPECTIVO VALOR(VALUE), A UM DICIONÁRIO
CampeãoBrasileiro = {2014: "Cruzeiro", 2015: "Corinthians", 2016:"Palmeiras", 2017:"Corinthians",
                        2018:"Palmeiras", 2019:"Flamengo", 2020:"Flamengo", 2021:"Atlético-MG"}
CampeãoBrasileiro[2022] = "Fluminense"
print(CampeãoBrasileiro)


#CONCATENAR TRÊS DICIONÁRIOS, CRIANDO UM NOVO DICIONÁRIO RESULTANTE
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

#opção 1
dicionario = {**dic1, **dic2, **dic3}
print(dicionario)

#opção 2
dicionario = dic1 | dic2 | dic3
print(dicionario)

#opção 3
dicionario = dict(dic1.items())
dicionario.update(dic2)
dicionario.update(dic3)
print(dicionario)


#PROGRAMA QUE CRIA DICIONÁRIOS LENDO CHAVES E VALORES E
#VERIFICA SE UMA CHAVE INFORMADA EXISTE EM UM DETERMINADO DICIONÁRIO
exemplo_dic = {k:k**2 for k in range(10)}

createDic = input("""
        Digite 1 para iniciar a criação de um dicionário. 
        Digite outro caracter para pesquisar chave em um dicionário: 
        """)
if createDic == "1":
    nameDic = input("Digite o nome do dicionário a ser criado: ")
    globals()[nameDic] = {}
    varloop = "S"
    while varloop == "S" or varloop == "s":
        tipo_chave = 0
        while tipo_chave > 3 or tipo_chave < 1:
            tipo_chave = int(input("""
                Se a chave for do tipo string, digite 1.
                Se a chave for do tipo int, digite 2.
                Se a chave for do tipo float, digite 3.
                """))
            if tipo_chave == 1:
                chave = input("Digite a chave do tipo string: ")
            elif tipo_chave == 2:
                chave = int(input("Digite a chave do tipo int: "))
            elif tipo_chave == 3:
                chave = float(input("Digite a chave do tipo float: "))
            else:
                print("Opção inexistente.")

        tipo_valor = 0
        while tipo_valor > 6 or tipo_valor < 1:
            tipo_valor = int(input("""
                Se o valor for do tipo string, digite 1.
                Se o valor for do tipo int, digite 2.
                Se o valor for do tipo float, digite 3.
                Se o valor for uma lista, digite 4 (nesse caso, a lista já deve existir previamente).
                Se o valor for uma tupla, digite 5 (nesse caso, a tupla já deve existir previamente).
                Se o valor for um set(conjunto), digite 6 (nesse caso, o set já deve existir previamente).
                """
                ))
            if tipo_valor == 1:
                valor = input("Digite o valor do tipo string: ")
            elif tipo_valor == 2:
                valor = int(input("Digite o valor do tipo int: "))
            elif tipo_valor == 3:
                valor = float(input("Digite o valor do tipo float: "))
            elif tipo_valor == 4:
                valor = input("Digite o nome de uma lista existente: ")
                valor = globals()[valor]
            elif tipo_valor == 5:
                valor = input("Digite o nome de uma tupla existente: ")
                valor = globals()[valor]
            elif tipo_valor == 6:
                valor = input("Digite o valor de um set existente: ")
                valor = globals()[valor]
            else:
                print("Opção inexistente.")

        globals()[nameDic].update(dict([(chave,valor)]))

        varloop = input("""
                Digite a letra S para acrescentar mais um conjunto (chave:valor). 
                Digite qualquer outro caracter para encerrar a criação do dicionário. 
                """)
        if varloop != "s" and varloop != "S":
            continue

else:
    pass

pesquisa = input("""
            Digite a letra S para realizar pesquisa em um dicionário.
            Digite outro caracter para sair 
            """)
        
while pesquisa == "s" or pesquisa == "S":
    nome_dicionario = input("Digite o nome do dicionário no qual será buscada a chave: ")
    tipo_chave = 0
    while tipo_chave > 3 or tipo_chave < 1:
        tipo_chave = int(input("""
            Se a chave for do tipo string, digite 1.
            Se a chave for do tipo int, digite 2.
            Se a chave for do tipo float, digite 3.
            """))
        if tipo_chave == 1:
            chave_pesq = input("Digite a chave do tipo string: ")
        elif tipo_chave == 2:
            chave_pesq = int(input("Digite a chave do tipo int: "))
        elif tipo_chave == 3:
            chave_pesq = float(input("Digite a chave do tipo float: "))
        else:
            print("Opção inexistente.")
        
    try:
        valor_chave = globals()[nome_dicionario][chave_pesq]
        print("A chave EXISTE e seu valor é: ", valor_chave)
    except:
        print("A chave pesquisada NÃO EXISTE.")
        
    pesquisa = input("""
                Digite a letra S para realizar uma nova pesquisa.
                Digite qualquer outro caracter para sair.
                """)


# ITERAR EM UM DICIONÁRIO UTILIZANDO LOOPS

# criando um dicionário
lista_chaves = ["nome", "cpf", "telefone", "endereço"]
lista_valores = ["José da Silva", "000.000.000-00", "(44) 9 ", ""]
Jose = dict(zip(lista_chaves, lista_valores))

# iterando em um dicionário
for chave in Jose:
    if Jose[chave] == None or Jose[chave] == "":
        print("A chave "+chave+" apresenta valor vazio. Favor informar valor correto")
    elif len(Jose[chave]) <= 10:
        print("A chave "+chave+" apresenta nº de caracteres muito pequeno. Possivelmente apresenta erro.")
    
    else:
        pass
print("Verificação concluída.")


#REMOVER REPETIDOS DE UMA LISTA
lista_ex = [9, 7, 5, 3, 0, 3, 1, 5, 10]

#Opção 1
i = 0
while i < len(lista_ex)-1:
    j=i+1
    while j < len(lista_ex):
        if lista_ex[i] == lista_ex[j]:
            lista_ex.pop(j)
        j+=1
    i+=1
print(lista_ex)

#Opção 2 (nesse caso os duplicados são eliminados, mas a ordenação inicial é perdida)
set_ex = set(lista_ex)
nova_lista = list(set_ex)
print(nova_lista) 


#VERIFICAR SE UMA LISTA ESTA VAZIA OU NÃO
nova_lista = []

def verif_lista (lista):
    if len(lista)>0:
        print("A lista não esta vazia")
    else:
        print("LISTA VAZIA")

verif_lista(nova_lista)


#CLONAR OU COPIAR UMA LISTA
uma_lista = [x for x in "tiago"]

#Opção 1
copia_uma_lista = uma_lista.copy()
print(copia_uma_lista)

#Opção 2 
clone_uma_lista = uma_lista[0:len(uma_lista)]
print(clone_uma_lista)