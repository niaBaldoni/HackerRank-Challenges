cube = lambda x: x**3

def fibonacci(n):
    lista = [0, 1]
    for i in range(2, n):
        lista.append(lista[i-2] + lista[i-1])
    return lista[0:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
