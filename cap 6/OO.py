#Continuando o projeto iremos ver agora como funciona alguns conceitos da
#orientação à objetos em python
# 
# O primeiro passo é criar uma classe
# usamos a palavra reservada class deninimos o nome da classe e o bloco de definição :

#Como estamos somente mostrando a estrutura básica não iremos implementar a classe
class MinhaPrimeiraClasse:
    pass 

#Para mais informações https://panda.ime.usp.br/pensepy/static/pensepy/13-Classes/classesintro.html

class MinhaSegundaClasse:
    #Dentro do bloco da classe podemos definir variáveis e funções
    #Para conseguirmos instânciar uma classe temos que ter um construtor
    #Em python um construtor é definido como def __init__(self, outro_parametros):

    def __init__(self, atributo1, atributo2 = False):
        #Todos método dentro de uma classe recebe o self como primeiro parâmetro
        self.atributo1 = atributo1 #Dessa forma será criado um atributo chamado atributo1 e ele receberá o valor de atributo1
        self.atributo2 = atributo2
        #Temos como definir um valor default

    #Esse é um exemplo de um método normal, lembrando que todos recebem como primeiro parâmetro o self
    def meuPrimeiroMetodo(self, parametro1):
        self.atributo1 = parametro1

    #python não tem suporte nativo para encapsulamento, ou seja, não possui atributos privados e publicos
    #todos os atributos e metodos podem ser vistos e acessados por fora da classe
    #mas existe uma convenção que os atributos e métodos que começam com __ são privados. Assim cabe o programador respeitar 
    #convenção e não acessar diretamente atributos ou métodos iniciados com __

#Python dá suporte para herança a sintaxe é class NomeClasseFilha(NomeClasseMae):
# 

class Mae:

    atributo_estatico = "Esse é um exemplo de atributo estático"

    def __init__(self, at1, at2):
        self.__at1 = at1
        self.__at2 = at2

    #Mesmo sem o suporte ao encapsulamento, python usa os seguintes modos para criar get e set respectivamente
    #Para mais informações entre no site https://www.treinaweb.com.br/blog/orientacao-a-objetos-em-python
    @property
    def at1(self):
        return self.__at1
    
    @at1.setter
    def at1(self, newAt1):
        self.__at1 = newAt1

    def mostrarNome(self, nome):
        print(nome + "da classe Mae")

class Filha(Mae):
    #Essa classe possui os mesmos atributos e métodos da classe Mae
    def __init__(self, at1, at2, at3):
        super().__init__(at1, at2) #Para acessar atributos ou métodos da classe Mae é só utilizar o super()
        self.__at3 = at3

    #Para usar o polimorfismo devemos usar a mesma assinatura como também os mesmos parametros
    # Em python não é suportado a sobrecarga de métodos, ou seja, só podemos ter um metódo com o mesmo nome, mesmo que tenha
    # diferentes parâmetros
    def mostrarNome(self, nome):
        print(nome + "da classe Filha")

#Pyhton dá suporte a herança multipla a sintaxe é class NomeClasseFilha(Prioridade1, Prioridade2):
#Onde a ordem das classes maes importam na hora de fazer a mesclagem(Mixin)

class MaisOutraClasse(MinhaPrimeiraClasse, MinhaSegundaClasse):
    pass

#Para criar classes abstratas devemos importar a seguinte biblioteca
from abc import ABC, abstractmethod

#E fazer uma classe que herde ABC

class ClasseAbstrata(ABC):

    def __init__(self, value):
        self.value = value

    @abstractmethod
    def metodoAbstrato(self):
        pass

