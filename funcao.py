def maiorEmLista(lista):
   """Retorna o maior número de uma lista."""
   i=1
   maior = lista[0]
   while i < len(lista):
      if maior < lista[i]:
         maior = lista[i]
      i+=1

   return maior




def somaLista(lista):
   """Retorna a soma dos números de uma lista."""
   soma = 0
   for numero in lista:
      soma = soma + numero

   return soma




def produtoLista(lista):
   """Retorna a soma dos números de uma lista."""
   produto = 1
   for numero in lista:
      produto = produto * numero

   return produto




def inverteString(string):
   """Retorna o inverso de uma string"""
   inverso = ""
   i = len(string)-1
   while i >=0:
      inverso = inverso+string[i]
      i-=1

   return inverso




def fatorial(valor):
   """Retorna o fatorial de um número"""
   fatorial = 1
   while valor > 0:
      fatorial = fatorial*valor
      valor -= 1
   
   return fatorial




def contaMAmi(string):
   """Conta a quantidade de letras maiúsculas e minúsculas de uma string(texto)"""
   MA = 0
   mi = 0
   for letter in string:
      if letter.isupper():
         MA +=1
      elif letter.islower():
         mi +=1
   printResultado(MA, mi)
   return MA, mi

def printResultado(MA, mi):
   """Mostra o resultado da função 'contaMaiuscMinusc'."""
   print("A quantidade de letras maiúsculas é: ", MA)
   print("A quantidade de letras minuscula é: ", mi)




def executaCodigo(string):
   """Executa uma string que é um código em Python"""
   exec(string)

codigo = """
nome = input("Digite seu nome: ")
print("Oi, "+nome+"!")
"""




def ehPrimo():
   """Recebe um número do console e diz se ele é primo ou não."""
   numero = int(input("Digite um numero natural maior que 1, para descobrir se ele é um número primo: "))
   resultado = True
   for n in range(2, int(numero/2)):
      if numero%n == 0:
         resultado = False
   
   return print(resultado)




def ehPerfeito(numero):
   """Retorna se um número é ou não perfeito."""
   resultado = True
   soma = 0
   for n in range(1, int(numero/2)+1):
      if numero%n == 0:
         soma = soma + n
  
   if soma != numero:
      resultado = False
   
   return resultado




def linhasTriPascal(n):
   """Retorna as n primeiras linhas do triângulo de Pascal"""
   # crio um dicionário para armazenar o resultado {1:[1], 2:[1,1],...}
   resultado = {}
   # como a primeira chave do dicionário deve ser um e a ultima n, 
   # sabendo que a função range  do python inclui o primeiro e exclui 
   # o último, faço range(1, n+1)
   for y in range(1, n+1):
   #digo que a chave y terá como valor uma lista
      resultado[y]=[]
      # aqui eu digo que a lista terá y termos
      for z in range(y):
         # aqui eu preecho todos os termos com o número um
         resultado[y].append(1)
      
      # sabemos que para y = 1 e y = 2, teremos todos os termos iguais a um,
      # e para os outros valores de y, sempre começaremos com um e terminaremos com um
      # então, quando y for maior que 2, teremos itens intermediários diferentes de um.
      if y > 2:
         # como o primeiro termo (indice 0) e o último termo (indice y-1), são um
         # eu não preciso alterá-los, portanto, para x, faço range(1, y-1)
         for x in range(1, y-1):
            # o triângulo de pascal diz que o item x da linha y, tem que ser a soma
            # do item x-1 da linha y-1 com o item x da linha y-1
            resultado[y][x] = resultado[y-1][x-1]+resultado[y-1][x]

   return resultado


r = linhasTriPascal(10)
for linha in r:
   print(r[linha])