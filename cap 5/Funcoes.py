# Nesta secção, iremos abordar os conceitos sobre funções em python, bem como sua criação.
# Funções ou rotinas servem para solucionar um problema que será bastante requisitado na sua aplicação.
# Por exemplo, podemos ter uma função que realiza a soma de dois números ou então apenas printa uma mensagem.
# Funções com nomes compostos devem ser separados por underscore _ e devem possuir as letras todas minusculas (boas pŕaticas)

#Uma função pode ser feita da seguinte forma

print("\nRESPOSTA EXEMPLO FUNÇÃO SEM RETURN\n")
def say_hi():
    print("Oi")  #perceba a identação.

say_hi()  # aqui estamos chamando nossa função. 

#RESULTADO ESPERADO : OI


#OBS: para um código ser lido dentro de uma função, ele deve estar indentado. Todo o código deve estar
#     abaixo dos dois pontos :


# Se você estiver usando uma IDE ou Visual Code por exemplo, verá que nesse seguinte código temos um erro.
# Ao analisarmos o erro, o Intelisense aponta que o comando print não está indentado.

#descomente as duas linhas abaixo para ver o erro 
#def say_hi():
#print("Oi")      #perceba que não está indentado com a função. Logo, esta linha não está no escopo da função.


# Como ja sabemos, python aceita qualquer tipo de dado em uma variavel, portanto, em uma função com parametros,
#   temos:

def say_my_name(name):
    print("Meu nome é: "+name)

say_my_name("Jonas")

#RESULTADO ESPERADO : Meu nome é Jonas

# Aqui, teremos um exemplo de utilização de uma função com o return
print("\nRESPOSTA EXEMPLO FUNÇÃO COM RETURN\n")
def soma( a,b):
    return a+b

print(soma(1,2))  #primeiro ocorre a chamada da função de soma, e o resultado retornado dela será printado

#RESULTADO ESPERADO : 3

######################################  TIPOS DE PARAMETROS  ##########################################################

# Em uma função podemos ter tipos de parametros. Temos o posicional(default),nomeados,comprimento variado, entre outros.

# Um parametro posicional é aquele que é obrigatório ser passado na chamada de uma função.
# Um parametro opcional é aquele que, caso nenhum dado seja atribuido a ele, ele ira usar o valor defenido a ele
# Observe que os parametros opcional devem ser colocados por ultimo na criação de uma função, para nao dar erro no interpretador.

# Exemplo
print("\nRESPOSTA EXEMPLO PARAMETRO OPCIONAL\n")
def parametro_opcional(a,b=2):   # a é posicional, e b é opcional
    return a+b

print(parametro_opcional(1,2))   #RESULTADO ESPERADO : 3
print(parametro_opcional(1))   #RESULTADO ESPERADO : 3..

#Como nao foi passado o valor de b na segunda chamada da função, foi utilizado o valor default definido b = 2

# No exemplo abaixo teremos o tipo de parametro de comprimento variado, onde claramente na chamada de sua função
#   estamos passando 4 argumentos, sendo que a função só possui 3 parametros. *args é um parametro que consegue abarcar varios valores

print("\nRESPOSTA EXEMPLO PARAMETRO COMPRIMENTO VARIADO\n")
def myfunction(first_name, last_name, *args):
    print(first_name)
    print(last_name)
    for argument in args:
        print(argument)

# Calling the Function 
myfunction('Tim','White',999888999,30, "amor")


#RESULTADO
    #Tim
    #White
    #999888999
    #3


#No exemplo abaixo, teremos o parâmetro nomeado. Argumento nomeado é a 
#   passagem de valores fazendo associação com o nome do parâmetro e o valor que está sendo enviado.

# Podemos ver que na chamada da função, passamos os valores posicionais de a=1 e b=2, porem, nomeamos
#   para qual parametro irão os valores 4 e 3. Nesse caso, d=4 e c=3.

# Parametros nomeados não precisam ser passados na chamada da função na forma sequencial, ou seja,
#  não é nescessário passar o argumento na ordem em que ele foi criado na função. Perceba que d=4 ocupa
#  o lugar onde deveria ser passado o valor de c. Mas devido a ser nomeado nessa chamada, podemos  colocar em
#  qualquer lugar após passar os valores posicionais(obrigatorios)

print("\nRESPOSTA EXEMPLO PARAMETRO NOMEADO\n")
def minha_func1(a, b, c, d):
    print(a, b, c, d)

minha_func1(1, 2, 3, 4)

#RESULTADO : 1 2 3 4

def minha_func2(a, b, c, d):
    print(a, b, c, d)

minha_func2(1, 2, d=4, c=3)

#RESULTADO : 1 2 3 4


############################################# PACKING E UNPACKING #######################################3

#Packing é uma forma de passarmos varios dados para uma função, e não sabemos quantos dados essa função pode receber.
#Ou seja, é o mesmo exemplo mostrado anteriormente usando o *args como parametro

#Exemplo

print("\nRESPOSTA EXEMPLO PACKING\n")
def mySum(*args):   # Não sabemos quantos argumentos devem ser passados, então devemos agrupalos na variavel *args
    return sum(args) #sum() é uma função que soma os elementos de um vetor
 
print(mySum(1, 2, 3, 4, 5)) #RESULTADO : 15
print(mySum(10, 20))  #RESULTADO : 30


#Unpacking é quando temos um agrupado de dados e queremos passa-los para os parametros de uma função. Exemplo

print("\nRESPOSTA EXEMPLO UNPACKING\n")
def fun(a, b, c, d):
    print(a, b, c, d)
 
my_list = [1, 2, 3, 4]
 
fun(*my_list)  #Ao fazermos isso, estamos pegando cada elemento da lista e passando para o respectiovo argumento
               # Basicamente temos : a = my_list[0], b = my_list[1], c = my_list[2], d = my_list[3]
 
#RESULTADO : 1, 2, 3, 4


#################################################### CALLABLE ##################################################

#É uma função que retorna verdadeiro se o seu argumento é pode ser chamado(função, construtor, etc) ou não

#Exemplo:
x = 5
print(callable(x))  #Falso, pois x não é algo que invoca alguma coisa

def testFunction():
  print("Test")

y = testFunction
print(callable(y))  #True, pois y é uma função e é algo que pode ser chamado/invocado


############################################ IMPORTANDO FUNÇÔES DE OUTROS ARQUIVOS #######################################

#O exemplo abaixo mostra como importar uma função vindo de outro arquivo no mesmo diretório.
#Ele pega a função teste_soma do arquivo Teste.py e a importa para este arquivo, fazendo com que possamos utiliza-la livremente.
from Teste import teste_soma

a = 2
b = 5
print(teste_soma(a,b)) #RESULTADO ESPERADO: 7