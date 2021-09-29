cart = []
item = ''
while item != 'quit':
    print('Add product or type quit to exit.')
    item = input()
    if item != 'quit':
        cart.append(item)

print('\n')
for item in cart:
    print(item)
