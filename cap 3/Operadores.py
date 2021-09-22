# Neste capítulo veremos sobre Operadores.
# Os operadores são usados na construção de expressões, veremos a seguir os operadores.

# -> Operadores Aritméticos

# São aqueles que realizam operações matemáticas como subtração, soma... Usaremos as variáveis n1 e n2 para exemplificar.
n1 = 7
n2 = 2

# Adição:
soma = n1 + n2
print(soma) # retorna 9

# Subtração:
sub = n1 - n2 
print(sub) # retorna 5

# Multiplicação:
multi = n1 * n2 
print(multi) # retorna 14

# Divisão
div = n1 / n2
print(div) # retorna 3.5

# Divisão inteira (os números após a vírgula não são mostrados, apenas a parte inteira)
divint = n1//n2
print(divint) #retona 3 ao invés de 3.5

# Módulo (retorna o resto da divisão inteira)
n1%n2 # retorna 1

# Exponenciação
n1**n2 # retorna 49

# -> Operadores Relacionais

# São eles: Maior que >, Menor que <, Igual a ==, Maior ou igual a >=, Menor ou igual a <= .
# Da seguinte forma faremos a relação: <membro a esquerda> OPERADOR <membro a direita>

print(n1 > n2) # n1 maior que n2 : true
print("a" > "b") # "a" maior que "b" : false
print(5 < 10) # 5 menor que 10 : true
print (200 == 200) # 200 igual a 200: true
print(12 >= 10) # 12 maior ou igual a 10: true
print(10 <= 16) # 10 menor ou igual a 16: true

# -> Operadores Atribuição

# O operador de atribuição em Python é aquele que dá valor a uma variável.

# 1 - Operador "="
x = 1 # a variável 'x' agora possui o valor 1 como podemos ver colocando o seguinte comando:
print(x)

# 2 - Operador "+="
x += 1 # a variável 'x' agora possui o valor 2 como podemos ver colocando o seguinte comando:

# 3 - Operador "-="
x -= 1 # x= x-1

# 4 - Operador "*="
x *= 1 # x= x*1

# 5  - Operador "/="
x /= 1 # x= x/1

# 6 - Operador "%="
x %= 1 # x= x%1

# -> Operadores Lógicos
# Os operadores lógicos são usados para unir duas ou mais expressões condicionais são eles: and, or, not.

# Operador AND: se <condição 1> for verdade e <condição 2> também for verdade retorna True, caso contrario retorna false.
(2>1) and (3>1) #retorna True
(2<1) and (3>1) #retorna False
(2<1) and (3<1) #retorna False

# Operador OR: se <condição 1> for verdade ou <condição 2> for verdade retorna True, caso contrario retorna false.
(2>1) or (3>1) #retorna True
(2<1) or (3>1) #retorna True
(2<1) or (3<1) #retorna False

# Operador NOT: inverte o resultado - se o resultado da expressão for True, o operador retorna false
not((2>1) and (3>1)) #retorna False
not((2<1) or (3<1)) #retorna True

# -> Operadores Unários
# Aceitam só um operando. Em Python, eles são -, +, ~, not (negação unária, positivo unário, negação bitwise e negação lógica)
x = False
y = not x  #  O operador “not” inverte o valor booleano de x.
print(y) # retorna True

a = -1
b = -a  #  O operador “-“ inverte o sinal de a.
print(b) # retorna 1



# -> Operadores Ternários
# São expressões condicionais, são necessários dois operandos e uma expressão.
# Possui a forma <operando1> if <expressão> else <operando2>.

a = 6
b = 3

'Não foi possível dividir' if b == 0 else a / b #como b não é igual a 0 a divisão foi efetuada e resultado igual a 2

#Mudando o valor de b para 0
b=0
'Não foi possível dividir' if b == 0 else a / b #retornará que 'não foi possível dividir'