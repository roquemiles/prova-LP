#Lista inteiro com Fibonacci

fibonacci = []
listaCerta = []
lista = []
numero = 1

while True:
    try:
        while True:
            numero = int(input("Digite um número inteiro (0 para sair): "))
            if numero < 0:
                print("Digite um valor maior que 0.")  
            elif numero == 0:
                break
            elif numero not in lista:
                lista.append(numero)
        break
    except ValueError:
        print("Digite um valor válido.")

a = len(lista)-1
i = 0
while a > i:
    j = 0
    while a > j:
        if (lista[j] > lista[j+1]):
            aux = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = aux
        j += 1    
    i += 1

i = 0
while a >= i:
    if lista[i] > 20:
        print(f"Está sequência de Fibonacci '{lista[i]}' não pode ser apresentada pois ultrapassa 20 posições.")
    else:
        j = 0
        termo1 = 0
        termo2 = 1
        print(f"Sequência de Fibonacci de {lista[i]} posições: ")
        fibonacci.clear()
        while j < lista[i]:
            if lista[i] == 1:
                resultado = termo1 + termo2
                termo2 = termo1
                termo1 = resultado
                print(resultado)
                break
            resultado = termo1 + termo2
            termo2 = termo1
            termo1 = resultado
            fibonacci.append(resultado)
            j += 1
        print(*fibonacci, sep=",")
    i += 1