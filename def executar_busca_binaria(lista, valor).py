def executar_busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista) - 1
    while minimo <= maximo:
        #encontra o elemento que divide a lista ao meio
        meio = (minimo + maximo)//2
        #verifica se o valor procurado esta na esquerda ou na direita do valor central
        if valor < lista [meio]:
            maximo = meio - 1
        elif valor > lista [meio]:
            minimo = meio + 1
        else:
            return True # se o valor for encontrado para aqui
    return False #se chegar ate aqui, quer dizer que o valor n foi encontrado
    
lista = list(range(1, 50))
    
print(lista)

print('\n', executar_busca_binaria(lista=lista, valor= 10))
print('\n', executar_busca_binaria(lista=lista, valor= 20))
