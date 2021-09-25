import time # para facilitar a visualização imprimindo lentamente os dados.

class Nodo: 
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)

class PilhaListaEncadeada: 
    def __init__(self):
        self.topo = None 
    def __repr__(self):
        return "[" + str(self.topo) + "]"
    def empilha(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        novo_nodo.anterior = self.topo
        self.topo = novo_nodo
    def desempilha(self):
        assert self.topo, "Impossível remover valor de pilha vazia." # caso tente remover de pilha vazia
        self.topo = self.topo.anterior
    def pilha_vazia(self):
        if(self.topo): # contendo um .topo no elemento pai quer dizer que a pilha não está vazia
            print("Pilha não está vazia")
        else:
            print("Pilha está vazia.")
    def ver_topo(self):
        if(self.topo): # é true se a pilha não estiver vazia (Obrigado Python <3)
            print("O valor no topo da pilha é: {0}".format(self.topo.dado))
        else:
            print("Pilha está vazia.")


pilha = PilhaListaEncadeada() # criando pilha como um tipo PilhaListaEncadeada
print("\n")
print("Pilha inicial vazia: ", pilha) # aqui eu printo ela só pra mostrar que está vazia
print("Para demonstrar o funcionamento insira 3 valores...")
a = "\n--------------------------\n" # defini isso aqui para printar quebras no código posteriormente
print(a)

# range abaixo é um valor que poderia ser definido pelo usuário ou mesmo dinâmico 
# eu coloquei 3 para facilitar o teste mas pode ser dinâmico.

for i in range(3): 
    pilha.empilha(int(input('Qual valor a ser empilhado?\t')))
print(a)
time.sleep(1)

# aqui eu chamo a função pilha_vazia que retorna o print dizendo se está vazia ou não.

print("Função pilha_vazia...")
pilha.pilha_vazia()
print(a)
time.sleep(2)

# aqui eu chamo a função ver_topo que vai retornar o self.topo.dado
# mostrando para o usuário apenas o conteúdo do elemento no topo da pilha

print("Função ver_topo...")
pilha.ver_topo()
print(a)
time.sleep(4)

# aqui eu chamo a função desempilhar e ver topo constantemente dentro do while 
# para mostrar os elementos se removendo.

print("Rodei a função desempilhar até limpar a pilha inteira...")
print(a)
while pilha.topo != None:
    pilha.ver_topo()
    pilha.desempilha()
    time.sleep(1)
pilha.ver_topo()
time.sleep(4)
print(a)

# agora com a pilha vazia eu peço pra ver se ela está vazia

print("Função pilha_vazia...")
pilha.pilha_vazia()
print(a)
time.sleep(3)