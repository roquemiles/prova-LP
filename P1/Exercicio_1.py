print("Exercício 1\n")

lista = []
lista2 = []
lfatorial = []
i = 0
a = 3

while i < 4:
    while True:
        try:
            numeros = int(input(f"Digite o {i+1}º número: "))
            lista.append(numeros)
            i+=1
            break
        except ValueError:
            print("Digite um valor válido.")

lista2 = lista.copy()

a = 3
while a > 0:
    j = 0
    while j < a:
        if (lista2[j] > lista2[j+1]):
            aux = lista2[j]
            lista2[j] = lista2[j+1]
            lista2[j+1] = aux
        j+=1
    a-=1

n = 0
while n < 4:
    f = 1
    resultado = 1
    while f <= lista2[n]:
        resultado = f * resultado
        f+=1
    n+=1
    lfatorial.append(resultado)

print(f"Lista digitada: \n{lista}")
print(f"Lista em ordem crescente: \n{lista2}")
print(f"Fatorial dos números da lista odenada: \n{lfatorial}")
