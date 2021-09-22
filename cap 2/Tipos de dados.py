# Neste capítulo falaremos sobre Estrutura e tipos de dados

# Váriaveis e tipos de dados
# Assim como outras linguagens de programação temos as váriaveis e os tipos de dados

# Variáveis

# Para criar uma variável em Python, tudo o que você precisa fazer é especificar o nome da variável e, em seguida, atribuir um valor a ela.
nome_da_variavel = 'valor da variável'

# O sinal de igual ‘=’ é usado para atribuir valores a variáveis. Assim sendo, não há necessidade de declarar uma variável antecipadamente. Atribuir um valor a uma variável em si declara e inicializa a variável com esse valor. Não há como declarar uma variável lhe atribuir um valor inicial.

# Tipos de dados básicos em Python:
# 1 - bool: pode assumir valor true ou false
# abaixo iremos comparar se o valor de a é menor que o valor de b, se é maior e se é igual, retornando assim um valor bool: true ou false.

a = 3
b = 4
c = a < b   # c recebe o valor da comparação a < b
d = a > b   # d recebe o valor da comparação a > b
e = a == b  # e recebe o valor da comparação a == b

print("Valor de c é ", c) # retorna true
print("Valor de d é ", d) # retorna false
print("Valor de e é ", e) # retorna false

# 2 - int: números inteiros como 1, 2, 3, 4... exemplo:

f = 5

# 3 - float: números reais como 1.2, 5.5...

g = 5.5

# 4 - str - string: que podem ser nomes, frases, entre outros, exemplo:

nome = 'Engenharia de Software é a melhor matéria'
print(nome)

# 5 - list - listas. Exemplo: [1, 2, 'ab']

lista = ['Petrolina','Juazeiro',25,1998]
lista #mostra a lista

# 6 - dict - dicionário: {'nome': 'João da Silva', 'idade': 21}

tradutor = {'three': 'tres', 'one': 'um', 'two': 'dois'} # atribui os valores em português para as palavras em inglês
tradutor['two'] # retorna dois
tradutor['one'] # retorna um
tradutor['three'] # retorna três

# 7 - NoneType - none

x = None
print(x) # saída: None

# Com isso aprendemos mais sobre variáveis e tipo de dados, no próximo capítulo aprenderemos mais sobre operadores.

