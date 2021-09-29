#  Nome: Samuel Cezar dos Santos
#  RA: 1996789

funcionarios = [] # fila de funcionários
tempoTotal = [] # fila de somatório dos tempos
clientes = [] # fila de clientes
contador = 0 # só uma variável contadora

x = input().split(" ") # input de n e m

x = input().split(" ") # tempo pra processar cada item
while True:
    try:
        funcionarios.append(int(x[contador])) # preenchimento da fila de funcionarios
        tempoTotal.append(0) # apenas criação dos valores da fila que marca o tempo total
        contador += 1
    except IndexError: # apenas pra controlar no caso de algum erro
        contador = 0
        break

x = input().split(" ") # quantos itens tem cada cliente

while True:
    try:
        clientes.append(int(x[contador])) # adiciona os clientes na fila de clientes
        contador += 1
    except IndexError: # apenas pra controlar no caso de algum erro
        cont = 0
        break
while True:
    try:
        tempoTotal[contador] = (funcionarios[contador] * clientes[0]) # joga para a fila tempoTotal o tempo do funcionário com o primeiro cliente da fila
        clientes.pop(0) # pula para o próximo cliente da fila
        contador += 1
    except IndexError: # apenas pra controlar no caso de algum erro
        break
while 0 < len(clientes): # inicia um loop que vai ler todo o vetor de clientes
    a = tempoTotal.index(min(tempoTotal))
    tempoTotal[a] = tempoTotal[a] + funcionarios[a] * clientes[0] # faz o cálculo total do tempo dos itens, funcionarios, e o primeiro cliente da fila 
    clientes.pop(0) # pula para o próximo cliente e assim vai até o fim da fila
print(max(tempoTotal)) # printa o maior resultado da fila de temposTotais