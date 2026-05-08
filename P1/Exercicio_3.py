print("Execício 3")
lista = []
lValorHora = []
lsalarioMes = []
i = 0
a = 0
j = 0
k = 0
print("Calcule seu salário dos ultimos 3 meses com desconto do INSS.")

while i < 3:
    while True:
        try:
            horas = int(input(f"Digite quantas horas você trabalhou no {i+1}º mês: "))
            if horas < 0:
                print("Digite um valor maior que zero.")
            else:
                lista.append(horas)
                i+=1
                break
        except ValueError:
            print("Digite um valor válido.")


while True:
    try:
        valorHora = int(input("Digite quanto vale sua hora de trabalho: "))
        if valorHora <= 0:
            print("Digite um valor maior que zero.")
        else:
            break
    except:
        print("Digite um valor válido.")

while a < 3:
    multi = valorHora * lista[a]
    lValorHora.append(multi)
    a+=1

while j < 3:
    if lValorHora[j] <= 1518:
        salario = lValorHora[j] - lValorHora[j] * 0.075
    elif lValorHora[j] < 2793.88:
        salario = lValorHora[j] - lValorHora[j] * 0.09
    elif lValorHora[j] < 4190.83:
        salario = lValorHora[j] - lValorHora[j] * 0.12
    elif lValorHora[j] < 8157.41:
        salario = lValorHora[j] - lValorHora[j] * 0.14
    else:
        salario = lValorHora[j] - 951.93
    lsalarioMes.append(salario)
    j+=1
    
while k < 3:
    print(f"Seu salário do {k+1}º mês é {lsalarioMes[k]}")
    k+=1
