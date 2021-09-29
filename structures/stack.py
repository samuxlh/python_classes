import time # just to print things slower

class Node: 
    def __init__(self, data=0, previous_node=None):
        self.data = data
        self.previous = previous_node

    def __repr__(self):
        return '%s -> %s' % (self.data, self.previous)

class stack: 
    def __init__(self):
        self.head = None 
    def __repr__(self):
        return "[" + str(self.head) + "]"
    def stackValue(self, new_data):
        novo_nodo = Node(new_data)
        novo_nodo.previous = self.head
        self.head = novo_nodo
    def unstackValue(self):
        assert self.head, "Can't remove from an empty stack."
        self.head = self.head.previous
    def is_empty(self):
        if(self.head):
            print("Stack is not empty.")
        else:
            print("Stack is empty.")
    def see_top(self):
        if(self.head):
            print("{0} is on top of the stack.".format(self.head.data))
        else:
            print("Stack is empty.")


pilha = stack() # criando pilha como um tipo stack
a = "___________________________________________________\n" # defini isso aqui para printar quebras no código posteriormente
print(a)

n = int(input('How many values you want to insert: '))

for i in range(n): 
    pilha.stackValue(int(input('insert value: ')))
print(a)
time.sleep(.5)

# aqui eu chamo a função is_empty que retorna o print dizendo se está vazia ou não.

print("Is stack empty?")
pilha.is_empty()
print(a)
time.sleep(3)

# aqui eu chamo a função see_top que vai retornar o self.head.data
# mostrando para o usuário apenas o conteúdo do elemento no head da pilha

print("What's on top of stack?")
pilha.see_top()
print(a)
time.sleep(3)

# aqui eu chamo a função desempilhar e ver head constantemente dentro do while 
# para mostrar os elementos se removendo.

print("Now I'll remove all elements individually.")
print(a)
while pilha.head != None:
    pilha.see_top()
    pilha.unstackValue()
    time.sleep(.5)
pilha.see_top()
time.sleep(3)
print(a)

print("Is stack empty?")
pilha.is_empty()
print(a)
time.sleep(3)