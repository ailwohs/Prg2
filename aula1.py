from random import randint

def preenche_matrix(c, l):
    matrix = [[0 for _ in range(c)] for _ in range(l)]
    for i in range(l):
        for j in range(c):
            matrix[i][j] = randint(100, 255)
    return matrix

def imprime_vet(vet):
    for i in range(len(vet)):
        print(vet[i])

matrix = [  [1,1,1,1,1], [2,2,2,2,2], [3,3,3,3,3],  [4,4,4]]

print(matrix)
print()
for i in range(len(matrix)):
    print(matrix[i], "->", len(matrix[i]))

print("depois de incluir o 8 na quarta linha")

matrix[3].append(8)
imprime_vet(matrix)


#faça a quantidade de elementos que tem na matriz

qtd_total = sum(len(linha) for linha in matrix)
print("Quantidade total de elementos na matriz:", qtd_total)

    
    
#faça~uma função que receba uma matriz e imrpima a quantidade de elementos

def conta_elementos(matrix):
    total = 0
    for linha in matrix:
        for _ in linha:
            total += 1
    print("Quantidade de elementos na matriz:", total)
conta_elementos(matrix)

#achar elemento de uma linha 
quantidade_linha0 = len(matrix[0])


# i = sempre é linha e o j = numero das colunas
