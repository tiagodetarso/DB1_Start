# EXERCÍCIO 01:
class NumeroInteiro:
    """Classe de números inteiros"""

    #correspondência entre número inteiro e símbolo dos números romanos
    correspondencia = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L',
                       90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}

    def __init__(self, inteiro:int):
        """Instancia um objeto com um número inteiro (int) como atributo"""
        self.inteiro = inteiro

    def romano(self):
        """Método para transformar número inteiro em número romano"""

        #Transforma as chaves do dicionário 'correspondencia' em uma lista de números inteiros
        valores = [keys for keys in NumeroInteiro.correspondencia.keys()]
        #Cria lista para armazenar o resultado
        resultado= []

        a = self.inteiro

        #faz a divisão do valor inteiro em equivalentes romanos
        while a != 0:
            for x in range(-1,-1-len(valores), -1):
                while a >= valores[x]:
                    if a >= valores[x]:
                        resultado.append(NumeroInteiro.correspondencia[valores[x]])
                        a = a - valores[x]

        #junta as strings da lista resultado 
        valor_final = "".join(resultado)
        #retorna a string gerada acima
        return valor_final     




# EXERCÍCIO 02:
class NumeroRomano:
    """Classe de números romanos"""

    #correspondência entre símbolo do número romano e número inteiro
    correspondencia = {"I":1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    def __init__(self, romano:str):
        """Instancia um objeto com um número romano (string) como atributo"""
        self.romano = romano

    def inteiro(self):
        """Método para transformar número romano em número inteiro"""

        #Cria listas para armazenar utilizadas para obter o resultado
        lista_valores = []
        resultado = []

        #faz a divisão do valor inteiro em equivalentes romanos
        for letra in self.romano.upper():
            lista_valores.append(NumeroRomano.correspondencia.get(letra))
        
        i = 0
        while i < len(lista_valores):
            if lista_valores[i] > lista_valores[i+1]:
                resultado.append(lista_valores[i])
                i+=1
            else:
                a = lista_valores[i+1] - lista_valores[i]
                resultado.append(a)
                i+=2

        valor_final = sum(resultado)

        return valor_final




# EXERCÍCIO 03:
class Numeros:
    """Classe de Números"""

    def __init__(self, num):
        """Instancia o objeto com um número como atribubo"""
        self.num = num
    
    def exponencial(self, outro):
        """Cálcula a exponcial de um número o objeto por um outro número"""
        # verifica se o atributo outro passado para a função é objeto dessa classe
        if isinstance(outro, Numeros):
            exp = self.num**outro.num
        else:
            exp = self.num**outro

        return exp




# EXERCÍCIO 04: 
class Strings:
    """Classe de elementos do tipo string"""
    def __init__(self, lista):
        """Instancia o objeto com uma string como atributo, que já é inserida em uma lista"""
        self.lista = [lista]
    
    def __str__(self):
        """Imprime a lista de palavras"""
        return ", ".join(self.lista)
    
    def adicionar(self, string):
        """Adiciona palavra à lista"""
        self.string = string

        self.lista.append(self.string)

        return self.lista
    
    def invertidas(self):
        """Inverte as palavras da lista e as apresenta em ordem contrária à de sua adição à lista"""
        invertidas = []

        for i in range (-1, -1-len(self.lista), -1):
            invertidas.append(self.lista[i][::-1])
        
        return invertidas




# EXERCÍCIO 05:
class Alunos:
    """Classe de Alunos de uma escola"""
    def __init__(self, id, nome=None, classe=None):
        """Instancia o objeto com os atributos id, nome e classe"""
        self.id = id
        self.nome = nome
        self.classe = classe
    
    def __str__(self):
        """Imprime os atributos id, nome e classe do objeto"""
        return "id: %s\nnome: %s\nclasse: %s." %(self.id, self.nome, self.classe)
"""
Tiago = Alunos('00001', 'Tiago T. R. Gonçalves', '2022-A')

print(type(Tiago))
print("=============")
print(type(Alunos))
print("=============")
print(Tiago.__dict__)
"""



# EXERCÍCIO 06:
class Triangulo:
    """ Classe de polígonos do tipo Triângulo"""
    def __init__(self, ang1, ang2, ang3):
        """Instancia um objeto com três ângulos (int) como atributos"""
        self.ang1 = ang1
        self.ang2 = ang2
        self.ang3 = ang3
    
    def __str__(self):
        if self.check_angulo():
            return "É, SIM, um triângulo com os seguintes ângulos: ang1= %dº, ang2= %dº, ang3= %dº." %(self.ang1, self.ang2, self.ang3)
        else:
            return "NÃO É um triângulo. Os ângulos do objeto são: ang1= %dº, ang2= %dº, ang= %dº." %(self.ang1, self.ang2, self.ang3)

    def check_angulo(self):
        if self.ang1 + self.ang2 + self.ang3 == 180:
            return True
        else:
            return False
"""
tri = Triangulo(90,45,45)
print(tri)
"""



# EXERCÍCIO 07:
class Musica:
    """Classe representa letras de música"""
    def __init__(self, nome, artista, lista_estrofes:list):
        self.nome = nome
        self.artista = artista
        self.lista_estrofes = lista_estrofes

    def canta_pra_mim(self):
        print("\nTítulo: "+self.nome)
        print("Artista: "+self.artista+"\n")
        print("\n\n".join(self.lista_estrofes)+"\n")
    
letra1 = ["E na cama quando inflama\nPor outro nome me chama\nMas tem fácil explicação\nO meu nome é Djair\nFacinho de confundir\nCom João do Caminhão.",
            "Veja só como é que é\nA ingratidão de uma mulher\nEla é o meu tesouro\nNós fomos feitos um para o outro\nEla é uma vaca e eu sou o touro."]
"""
BDC_MAss = Musica("Bois Don`t Cry", "Mamonas Assassinas", letra1)
BDC_MAss.canta_pra_mim()
"""



# EXERCÍCIO 08
from datetime import datetime
class JatoMilitar1Lugar:
    """Classe que representa Jatos Militares de um lugar"""
    def __init__(self, modelo, base_orig):
        self.modelo = modelo
        self.base = base_orig
        self._historico = [self.base]
        self._designa = False
    
    def designar_piloto(self, piloto):
        self.piloto = piloto
        self._designa = True
    
    def rebasear_aeronave(self, base_nova):
        if self._designa:
            self.base = base_nova
            self._data = datetime.now().strftime('%d-%m-%Y')
            self._hora = datetime.now().strftime('%H:%M')
            self._historico.append([self.base, self._data, self._hora])
            self._designa = False
        
        else:
            return print("Não foi possível rebasear a aeronave pois não há piloto designado.")
    
    def __str__(self):
        return """ 
                Jato: %s
                Base de Origem: %s
                Histórico de Transferências: %s
                """ % (self.modelo, self._historico[0], self._historico[1::])

jato1 = JatoMilitar1Lugar('TT16', 'Curitiba')
jato1.designar_piloto('Francisco José')
jato1.rebasear_aeronave('São Paulo')
print(jato1)



# EXERCÍCIO 09:
from datetime import datetime
class JatoMilitar2Lugares:
    """Classe que representa Jatos Militares de um lugar"""
    def __init__(self, modelo, base_orig):
        self.modelo = modelo
        self.base = base_orig
        self._historico = [self.base]
        self._designa = False
    
    def designar_pilotos(self, piloto, co_piloto):
        self.piloto = piloto
        self.co_piloto = co_piloto
        self._designa = True
    
    def rebasear_aeronave(self, base_nova):
        if self._designa:
            self.base = base_nova
            self._data = datetime.now().strftime('%d-%m-%Y')
            self._hora = datetime.now().strftime('%H:%M')
            self._historico.append([self.base, self._data, self._hora])
            self._designa = False
        
        else:
            return print("Não foi possível rebasear a aeronave pois não há piloto designado.")
    
    def __str__(self):
        return """ 
                Jato: %s
                Base de Origem: %s
                Pilotos: %s e %s
                Histórico de Transferências: %s
                """ % (self.modelo, self._historico[0], self.piloto, self.co_piloto, self._historico[1::])

jato2 = JatoMilitar2Lugares('RG07', 'Curitiba')
jato2.designar_pilotos('Edson Arantes do Nascimento','Ronaldo de Assis' )
jato2.rebasear_aeronave('São Paulo')
print(jato2)
