# A tupla deve ser definida ([]), depois de atribuir os valores não pode ser alterado
ns = tuple([1, 2, 8, 7, 6, 4, 6, 420])

for x in range (len(ns)):
    if ns[x] == 6:
        print(f"O elemento de índice {x} é igual a 6")