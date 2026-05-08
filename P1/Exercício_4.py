import random

print("Exercício 4")
lista = []
listRandom = []
liguais = []
a = 0
iguais = 0

print("Digite 6 números de 1 à 60")
while a < 6: 
    numero = int(input(f"Digite {a+1}º número: "))
    if numero < 1 or numero > 60:
        print("Digite um número de 1 à 60.")
    else:
        lista.append(numero)
        a+=1

for i in range(6):
    sorteio = random.randint(1,60)
    j = 0
    while j < 6:
        if sorteio == lista[j]:
            iguais+= 1
            liguais.append(sorteio)
        j+=1
    listRandom.append(sorteio)

print(f"\nLista digitada pelo usuário: {lista} \nLista sorteada: {listRandom} \nQuantidade de números presentes em ambas listas: {iguais}")
if len(liguais) > 0:
    print(f"Números em ambas as listas: {liguais}")
