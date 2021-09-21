#Continuando o projeto iremos ver agora as estruturas de controleem python
# 
# A primeiro, e maibasica dasa estruturas é o if-elif-else:
# Diferente de outras linguagens a parte de operação logica do if não precisa estar 
# dentro de parênteses, também não há necessidade de colocar abre e fecha chaves

# Para of comando if
# if <operação logica> :
#    <Comandos>

# exemplo 
a = 10 #para não ter erro por falta de variavel
if a==10:
    print("IF")

# O elif é o comando que implementa o comando "else if()", como um só.
# A estrutura if-elif também é usada como substituto para a estrutura 
# de controle switch, que não existe em pythom
# if <operação logica 1> :
#    <Comandos>
# elif <operação logica 2>
#    <Comandos>
# elif <operação logica 2>
#    <Comandos>
#    ...
# elif <operação logica N>
#    <Comandos>
# exemplo 

if a==1:
    print("IF 1")
elif a == 2:
    print("elif 1")
elif a == 3:
    print("elif 2")

# Se quiser recriar algo mais semelhante ao switch, ou simplismente quer
# reduzir o número de ifs e elifs usados, pode utilizar da outra fora de
# declaração do if:
# {<valor 1>: <comandos 1>,<valor 2>: <comandos 2>,...,<valor n>: <comandos n>}[<Operação / váriavel>]
# Exemplos:

print({1: "caso 1", 2: "caso 2", 3: "caso 3"}[a])

print({1: "caso 1", 2: "caso 2", 3: "caso 3"}[a+1])

# O else contiunua atuar como sempre, colocando para realizar ações 
# quando não entra nos ifs ou nos elifs, só pode ter um
# if <operação logica 1> :
#    <Comandos>
# elif <operação logica 2>
#    <Comandos>
# elif <operação logica 2>
#    <Comandos>
#    ...
# else:
#    <Comandos>
# exemplo 

if a==10:
    print("IF 1")
elif a == 1:
    print("elif 1")
else:
    print("else 1")

# O segundo é um dos comando de loop, o for:
# Diferente de como é declarado em outras linguagens é necessario usar uma 
# lista para gerar o loop,a variavel indicada no comnado for muda seu valor 
# pelos elementos que estão dentro da lista, do primeiro ao último, sempre 
# em passo 1, mesmo assim é possível simular para passos diferentes
# dependendo da lista usada, ecemplo:
# [1,2,3,4,5,...] lista passo 1
# [1,3,5,7,9,...] lista que simula passo 2

# Os valores dentro da lista não precisam ser números inteiros, eles podem 
# pertencer a qualquer tipo. 
# A lista pode ser declarada dentro do comando for ou passada por váriavel

# for x in <lista>:
#    <comandos>

# Seguem os exemplos:
l = ["a","b","c","d"]

for n in l:
    print(n+" ")
# A saída deve ser:a b c d 

for n in [1.1,2.1,3.4,4.8]:
    print(n+" ")
# A saída deve ser:1.1 2.1 3.4 4.8 

# Alguns comandos que geram listas automaticamente são utilizados em conjunto 
# com o for, para facilitar e agilizar a montagem deste. O mais usado é o range(),
# que produz uma lista de números inteiros a partir do 0 e possui duas formas de uso:
# No primero modo, o comando gera uma lista de inteiros até um valor maximo N, range(N) 

for n in range(3):
    print(n+" ")
# A saída deve ser:0 1 2 3  

# No segundo modo, o comando gera uma lista de inteiros de um valor inicial A 
# até um valor final B seguindo um passo N, range(A,B,N) 

for n in range(3,9,3):
    print(n+" ")
# A saída deve ser:3 6 9 

# Outro ponto que diferencia o uso do comando for é ques este também pode ser 
# acompanhado por um else, os que se encontrar dentro dele é execultado quando
# o loop do for termina normalmente, ele só é pulado se durante o loop o comando
# break for encontrado. 

# Antes de seguir, uma pequena relebrada dos comandos break e continue
# O comando break encerra uma operação de loop, o processo sai dela
# O comando continue retorna ao inicio do loop pulando tudo o que tem abaixo

#Exemplo:

for i in range(5):
    if a<2:continue #Impede que sejam impressos números menores que 2
    if a==3: break  #Impede que 3 seja impresso e encerra o loop
else:
    print(i+" ")
# A saída deve ser:2

# A terceira, e última, estrutura de controle é o while.
# Não exite muita diferença em seu funcionamento quanto a outras linguagens,
# ele execulta enquanto a operação lógica for verdadeira, os comando break
# e continue são usando em conjunto para controle de operações.
# Quanto a declaração, que nem o if, não há necesidade de parênteses nem chaves.

# Para o while:
# while <operação lógica>:
#   <comandos>

# Exemplo
while a<20:
    print(a+" ")
    a += 1
