def conta_elementos(matrix):
    qtd_total = 0
    for linha in matrix:
        qtd_total += len(linha)
    print("Quantidade de elementos na matriz:", qtd_total)


# Exemplo de uso
matrix = [
    [1,1,1,1,1],
    [2,2,2,2,2],
    [3,3,3,3,3],
    [4,4,4]
]

conta_elementos(matrix)
