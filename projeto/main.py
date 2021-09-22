# coding=UTF-8
# encoding: utf-8

#Este projeto serve para testar seus conhecimentos adquiridos até agora
#Primeiro rode o programa e responda-o
#Depois visualize como ele foi feito
#Preste atenção e revise os conceitos que foram trabalhados até agora como:
#classe, atributo, método, função, parametros nomeados, parametros opcionais, laços de repetição (for e while),
#if, else, operadores, incremento, tipos de dados
#Use seus conhecimentos para fazer alterações no código
#Você pode otimizá-lo ou acrescentar mais coisas
#Bons estudos!!

class Questao:
    def __init__(self, texto = "", palavras = [], outrasPalavras = [], numeroCorreto = -1):
        self.texto = texto
        self.palavras = palavras
        self.outrasPalavras = outrasPalavras
        self.numeroCorreto = numeroCorreto

    def mostrarTexto(self):
        print("Texto:\n\n\t%s\n" % self.texto.replace("\n","\n\t"))

    def mostrarOpcoes(self):
        numero = 1
        print("Selecione uma das seguintes opções:\n")
        for aux in self.outrasPalavras:
            print("\t%d - %s, %s" % (numero, aux[0], aux[1]))
            numero += 1
        
    def getResposta(self):
        self.mostrarTexto()
        self.mostrarOpcoes()
        resposta = int(input("\nDigite sua resposta:\n"))
        if resposta == self.numeroCorreto:
            print("Parabens você acertou!!")
        else:
            print("Você errou!!")
            resposta2 = input("Deseja tentar de novo? S/N\n")
            if resposta2 == "S":
                self.mostrarOpcoes()
                self.getResposta()

TEXTOS = [Questao(texto="Sempre que você chama uma __1__, você deve passar alguns __2__\npara aquela __1__ dependendo se a __1__ recebe algum __2__ ou não.\nNão é obrigatório passar um __2__ para uma __1__.",
    palavras = ["funções", "argumentos"],
    outrasPalavras = [["bloco", "problemas"],["modulo", "argumentos"], ["funções", "argumentos"],["procedimento", "inteiros"]],
    numeroCorreto = 3),
    Questao(texto="O __1__ serve para enviarmos cada dado de um agrupado de \ndados para uma função. Para isso, sabemos que a função deve possuir uma \nquantidade de __2__ equivalente ao tamanho do agrupado de dados.",
    palavras= ["unpacking", "parametros"],
    outrasPalavras= [["unpacking","valores"], ["unpacking","parametros"], ["packing","parametros"],["Packing", "funções"]],
    numeroCorreto=2),
    Questao(texto="Parametros __1__ são parametros que possuem valores pré-definidos na função e parametros __2__ são aqueles que possuem nomes",
    palavras= ["opcionais", "nomeados"],
    outrasPalavras= [["posicionais","nomeados"], ["opcionais","posicionais"],["de comprimento variado", "opcionais"], ["opcionais","nomeados"]],
    numeroCorreto=4),
    Questao(texto="Sabemos que o *args é um parâmetro de __1__. É muito utilizado ao fazer __2__.",
    palavras= ["comprimento variavel", "packing"],
    outrasPalavras= [["comprimento variavel","packing"], ["comprimento não variavel","unpacking"],["comprimento não variavel", "packing"], ["comprimento variavel","unpacking"]],
    numeroCorreto=1),
    ]

def percorrer_lista_questoes(listaQuestoes = []):
    print("\n\nBem-vindo ao teste.\n\n")
    contador = 1
    for questaoAtual in listaQuestoes:
        print("Questão Nº %d\n" % contador)
        questaoAtual.getResposta()
        contador += 1
    
def main():
    percorrer_lista_questoes(TEXTOS)

if __name__ == "__main__":
    main()