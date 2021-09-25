import time # importo essa biblioteca para facilitar a visualização dos elementos em console

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.prev = None
class FilaListaEncadeada:
    def __init__(self):
        self.head = None
        self.last = None
    def printfila(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" -> ")
            time.sleep(0.3)
            temp=temp.next
        print("\n")
    def enfileirar(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last.next.prev = self.last
            self.last = self.last.next
    def desenfileirar(self):
        if self.head is None:
            return ("Lista vazia")
        else:
            if self.head.next is not None:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
            
    def ver_inicio(self):
        return self.head.data
    def fila_vazia(self):
        if self.head is None:
            return True
        else:
            return False

# Declaro Fila como um tipo FilaListaEncadeada e o printo vazio mesmo.

Fila = FilaListaEncadeada()
print("\nFila inicial:")
time.sleep(0.3)
Fila.printfila()
time.sleep(0.8)

# Peço apenas 3 valores para o usuário mas poderia ser dinâmico
# logo abaixo os adiciono usando a função enfileirar
# por ultimo printo a fila novamente pra mostrar as inserções

print("Por favor insira 3 valores na fila...")
time.sleep(0.3)
for i in range(3):
    x = int(input("Valor: "))
    Fila.enfileirar(x) # o valor de x inserido pelo user dentro desse loop é enfileirado
print("\nFila após as 3 inserções...")
time.sleep(0.3)
Fila.printfila()
time.sleep(3)

# Aqui eu verifico se a fila está vazia.

print("\n\nFila está vazia?")
time.sleep(0.8)
print(Fila.fila_vazia()) # retorna um bool se tem um self.head ou n
time.sleep(3)

# Aqui eu verifico se a fila está vazia.

print("\nQuem está no início da fila?")
time.sleep(0.8)
print(Fila.ver_inicio()) # retorna self.head.data
time.sleep(3)

# Aqui eu revezo entre printar e desenfileirar para ilustrar 
# os elementos sendo removidos

print("\nAgora vou desenfileirar todos os elementos...\n")
time.sleep(0.8)
Fila.desenfileirar()
Fila.printfila()
Fila.desenfileirar()
Fila.printfila()
Fila.desenfileirar()
Fila.printfila()
time.sleep(3)

# Pergunto novamente se a fila está vazia

print("\n\nFila está vazia?")
time.sleep(0.8)
print(Fila.fila_vazia())
time.sleep(3)