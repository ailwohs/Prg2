import random

def gerar_array(tamanho):
    return [random.randint(1, 100) for _ in range(tamanho)]

def soma_array(array):
    soma = 0
    for n in array:
        soma += n
    return soma

def media_array(array):
    return soma_array(array) / len(array)

def inverte_array(array):
    inv = []
    for i in range(len(array)-1, -1, -1):
        inv.append(array[i])
    return inv

def imprime_array(array):
    for e in array:
        print(e)

def maior_array(array):
    m = array[0]
    for n in array:
        if n > m:
            m = n
    return m

def menor_array(array):
    m = array[0]
    for n in array:
        if n < m:
            m = n
    return m

if __name__ == "__main__":
    vetor = gerar_array(10)
    imprime_array(vetor)
    print("Invertido:")
    imprime_array(inverte_array(vetor))
    print("Soma:", soma_array(vetor))
    print("Média:", media_array(vetor))
    print("Menor:", menor_array(vetor))
    print("Maior:", maior_array(vetor))


print(len([1,2,3]))
v = [1,2,3]
v.append(4)
print(v)
v.insert(1, 99)
print(v)
v.extend([5,6])
print(v)
v.pop()
print(v)
v.remove(99)
print(v)
v.sort()
print(v)
v.reverse()
print(v)
