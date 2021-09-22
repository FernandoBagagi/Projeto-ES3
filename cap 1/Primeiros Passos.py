# Capítulo 1 - Primeiros passos na linguagem.
# Neste capitulo você verá o primeiro exemplo de código em python
# Para começarmos precisamos entender melhor sobre a linguagem, Python é uma linguagem de programação de alto nível, ou seja, com sintaxe mais simplificada e próxima da linguagem humana, utilizada nas mais diversas aplicações, como desktop, web, servidores e ciência de dados.
# Ele foi lançado no início dos anos noventa pelo programador e matemático holandês Guido Van Rossum. A linguagem foi projetada para dar ênfase no trabalho do desenvolvedor, facilitando a escrita de um código limpo, simples e legível, tanto em aplicações menores quanto em programas mais complexos.

#Python interpretado ou compilado?

# Você provavelmente já ouviu ou leu em algum lugar que Python é uma linguagem interpretada ou uma linguagem de script. Python é uma linguagem interpretada mas, assim como Java, passa por um processo de compilação.
# O interpretador é encarregado de fazer uma 'tradução' em tempo real para código de máquina, ou seja, em tempo de execução. Já o compilador traduz o programa inteiro em código de máquina de uma só vez e então o executa, criando um arquivo que pode ser rodado (executável). O compilador gera um relatório de erros (casos eles existam) e o interpretador interrompe a tradução quando encontra um primeiro erro.

# Agora veremos o primeiro exemplo de código em Python, sim, teremos nosso famoso "Olá mundo" também em Python, ele é da seguinte forma:

print('Olá, mundo!')

# Não tem muita diferença, né? E como percebeu o ponto e vírgula aqui não é necessário, na realidade é sabemos onde começa e termina determinado comando através da indentação.
# Indentação é uma forma de arrumar o código, fazendo com que algumas linhas fiquem mais à direita que outras, à medida que adicionamos espaços em seu início. Para a maioria das linguagens a indentação não é obrigatória, mas no caso Python isso é diferente.
# Em Python, a indentação possui função bastante especial, até porque, os blocos de instrução são delimitados pela profundidade da indentação, isto é, os códigos que estiverem rente a margem esquerda, farão parte do primeiro nível hierárquico. Já, os códigos que estiverem a 4 espaços da margem esquerda, estarão no segundo nível hierárquico e aqueles que estiverem a 8 espaços, estarão no terceiro nível e assim por diante.
# Um exemplo de indentação:

print('oi')#primeiro nível hierárquico

if(True):
    print('tchau')#segundo nível hierárquico

# Percebemos então que se não houvesse a indentação o código acima não funcionaria da maneira desejada, ou seja indentação não é opcional em Python.

# Como foi feito desde o início desse texto os comentários em Python são precedidos do símbolo: "#", sem estar precedido o comando pode ser executado.
