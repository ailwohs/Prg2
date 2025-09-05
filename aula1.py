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



mat = preenche_matrix(4, 3)
imprime_vet(mat)
