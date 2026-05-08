#Programa Loja

listaNomeVendidos = []
listaValorVendidos = []

print("## Escolha uma das opções para gerenciar a loja ## ")
print("- Digite '1' para cadastrar um produto vendido")
print("- Digite '2' para listar todos os produtos vendidos com seus valores")
print("- Digite '3' para calcular o valor total das vendas realizadas")
print("- Digite '4' para calcular o valor médio das vendas")
print("- Digite '5' para mostrar o produto mais caro e o produto mais barato vendido")
print("- Digite '6' para sair do programa")

while True:
    try:
        while True:
            escolha = int(input("Qual opção deseja escolher?: "))
            break
    
        if escolha == 1:
                while True:
                    nome = input("Digite o nome do produto vendido: ")
                    listaNomeVendidos.append(nome)
                    while True:
                        try:
                            while True:
                                valor = float(input("Valor do produto: ")) 
                                if valor <= 0:
                                    print("Digite um valor positivo.")
                                else:
                                    listaValorVendidos.append(valor)
                                    print("### Produto cadastrado ###")
                                    break
                            break
                        except ValueError:
                            print("Digite um valor válido.")
                    outroProduto = input("Deseja cadastrar outro produto? (S) ou (N): ")
                    if outroProduto == "N" or outroProduto == "n":
                        break
                    
        elif escolha == 2:
            if len(listaNomeVendidos) == 0:
                print("!!! Nenhum produto vendido !!!")
            else:
                print("Lista dos produtos vendidos: ")
                i = 0
                while i < len(listaNomeVendidos):
                    print(listaNomeVendidos[i], listaValorVendidos[i], sep=" - R$")
                    i += 1
                    
        elif escolha == 3:
            if len(listaNomeVendidos) == 0:
                print("!!! Nenhum produto vendido !!!")
            else:
                print("Valor total das vendas realizadas: ")
                valorTotal = sum(listaValorVendidos)
                print(f"R$ {valorTotal:.2f} em produtos vendidos.")
                
        elif escolha == 4:
            if len(listaNomeVendidos) == 0:
                print("!!! Nenhum produto vendido !!!")
            else:
                print("Valor médio das vendas: ")
                valorMedio = sum(listaValorVendidos) / len(listaNomeVendidos)
                print(f"R${valorMedio:.2f}")
                
        elif escolha == 5:
            if len(listaNomeVendidos) == 0:
                print("!!! Nenhum produto vendido !!!")
            else:
                a = len(listaValorVendidos)-1
                i = 0
                while a > i:
                    j = 0
                    while a > j:
                        if (listaValorVendidos[j] > listaValorVendidos[j+1]):
                            aux = listaValorVendidos[j]
                            listaValorVendidos[j] = listaValorVendidos[j+1]
                            listaValorVendidos[j+1] = aux

                            aux2 = listaNomeVendidos[j]
                            listaNomeVendidos[j] = listaNomeVendidos[j+1]
                            listaNomeVendidos[j+1] = aux2
                        j += 1    
                    i += 1
                print(f"O produto {listaNomeVendidos[0]} é o mais barato.")
                print(f"O produto {listaNomeVendidos[-1]} é o mais caro.")
                
        elif escolha == 6:
            print("Programa encerrado.")
            break
            
        else:
            print("!!! Digite um número da tabela !!!")
            
    except ValueError:
        print("Digite um valor válido.")