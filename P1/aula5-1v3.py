
from datetime import datetime, timedelta
import os

# Define caminho fixo do arquivo TXT na mesma pasta do arquivo
ArquivoTarefas = os.path.join(os.path.dirname(os.path.abspath(__file__)),"ListaAtiv.txt")

class Tarefa:
    def __init__(self, descricao, prazo):
        self.descricao = descricao
        self.prazo = prazo
        self.lembrete = None

    def definir_lembrete(self, lembrete):
        self.lembrete = lembrete

agenda = []

# Função para carregar tarefas do arquivo
def carregar_agenda():
    agenda.clear()
    try:
        with open(ArquivoTarefas,'r') as arqEntr: # abre o arquivo para leitura
            part1 = arqEntr.readline().strip() # lê a primeira linha
            while part1 != '':
                part2 = arqEntr.readline().strip() # lê a segunda linha
                part3 = arqEntr.readline().strip() # lê a terceira linha

                part2 = datetime.strptime(part2, "%Y-%m-%d %H:%M:%S")
                if part3 != "None":
                    part3 = datetime.strptime(part3, "%Y-%m-%d %H:%M:%S")
                else:
                    part3 = None

                tarefa = Tarefa(part1,part2)
                tarefa.definir_lembrete(part3)
                agenda.append(tarefa)
                part1 = arqEntr.readline().strip() # lê a primeira linha        
  #  arqEntr.close() # fecha arquivo
    except FileNotFoundError:
        print("Arquivo de tarefas não encontrado.")
    except Exception as e:
        print(f"Erro ao carregar tarefas: {e}")

# Função salvar tarefas no arquivo
def salvar_agenda():
    with open(ArquivoTarefas,"w") as arq:
        for t in agenda:
            arq.write(f"{t.descricao}\n")
            arq.write(f"{t.prazo}\n")
            arq.write(f"{t.lembrete}\n")

# Função para adicionar uma tarefa à agenda
def adicionar_tarefa():
    arq = open(ArquivoTarefas,'a')
    descricao = input("Digite o que você precisa fazer: ")

    try:
    # Converte a data do prazo para um objeto datetime
        prazo = datetime.strptime(input("Até quando você precisa terminar? (formato: DD/MM/AAAA): "), "%d/%m/%Y")
    except ValueError:
        print("Data inválida! Tarefa não adicionada.")
        return

    tarefa = Tarefa(descricao,prazo)

    if input("Quer receber um lembrete para essa tarefa? (sim/não): ").lower() == "sim":
        try:
        # Converte o lembrete para um objeto datetime
            lembrete = datetime.strptime(input("Quando você quer ser lembrado? (formato: DD/MM/AAAA HH:MM): "), "%d/%m/%Y %H:%M")
            tarefa.definir_lembrete(lembrete)
        except ValueError:
            print("Formato de lembrete inválido. Nenhum lembrete adicionado.")

    agenda.append(tarefa)
    arq.write(f"{tarefa.descricao}\n{tarefa.prazo}\n{tarefa.lembrete}\n")
    print("Tarefa adicionada com sucesso.")
    arq.close()

# Função para editar tarefa
def editar_tarefa():

    carregar_agenda() # Executar função carregar_agenda

    if not agenda:
        print("Nenhuma tarefa para editar.")
        return

    for i, tarefa in enumerate(agenda):
        print(f"{i+1} - {tarefa.descricao} - {tarefa.prazo}")

    try:
        indice = int(input(" Digite o número da tarefa que você quer editar: ")) - 1
    except ValueError:
        print("Entrada inválida")
        return

    if indice >= 0 and indice < len(agenda):
        tarefa = agenda[indice]
        print(f"Descrição cadastrada: '{tarefa.descricao}'")
        nova_descricao = input("Digite a nova descrição da tarefa: ")
        if len(nova_descricao) == 0:
            nova_descricao = tarefa.descricao
        tarefa.descricao = nova_descricao

        print(f"Prazo Cadastrado: '{tarefa.prazo.strftime('%d/%m/%Y')}'")
        novo_prazo = input("Digite o novo prazo da tarefa (formato: DD/MM/AAAA):").strip()
        if novo_prazo:
            try:
                tarefa.prazo = datetime.strptime(novo_prazo, '%d/%m/%Y')
            except ValueError:
                print("Formato de data inválido. Prazo mantido.")
#        if not novo_prazo:
#           novo_prazo = tarefa.prazo
#       else:
#            novo_prazo = datetime.strptime(novo_prazo, '%d/%m/%Y')
#        tarefa.prazo = novo_prazo
        if input("Deseja definir um novo lembrete para essa tarefa? (sim/não): ").lower() == "sim":
            try:
                novo_lembrete = datetime.strptime(input("Digite a nova data do lembrete (formato: DD//MM/AAAA HH:MM): "), "%d/%m/%Y %H:%M")
                tarefa.definir_lembrete(novo_lembrete)
            except ValueError:
                print("Formato de lembrete inválido. Nenhuma alteração feita.")

        print("Tarefa editada com sucesso! ")

        # Reescreve o arquivo na agenda atualizada
        salvar_agenda()

    else:
        print(" Número da tarefa inválido!! ")

# Função para remover tarefa 
def remover_tarefa():

    carregar_agenda() # Executar função carregar_agenda
    if not agenda:
        print("Nenhuma tarefa na agenda.")
        return

    for i, tarefa in enumerate(agenda):
        print(f"{i+1} - {tarefa.descricao} - {tarefa.prazo}")

    try:
        indice = int(input(" Digite o número da tarefa que você quer remover: ")) - 1
    except ValueError:
        print("Entrada inválida.")
        return
    
    if indice >= 0 and indice < len(agenda):
        tarefa = agenda.pop(indice)
        print(f"Tarefa '{tarefa.descricao}' removida com sucesso! ")

        # Reescreve o arquivo na agenda atualizada
        salvar_agenda()

    else:
        print("Número da tarefa inválido. ")


# Função para exibir as tarefas pendentes
def exibir_tarefas_pendentes():

    carregar_agenda() # Executar função carregar_agenda
    if not agenda:
        print("Nenhuma tarefa na agenda.")
        return


    if len(agenda) == 0:
        print("Não há tarefas pendentes.")
    else:
        print("Suas tarefas pendentes são: ")
        for tarefa in agenda:
            print(f" Descrição: {tarefa.descricao}")
            print(f" Prazo: {tarefa.prazo.strftime('%d/%m/%Y')}")
#            if tarefa.lembrete != "None":
            if tarefa.lembrete:
                print(f" Lembrete: {tarefa.lembrete.strftime('%d/%m/%Y %H:%M')}")
            print()

# Função para verificar lembretes próximos
def verificar_lembretes_proximos():

    carregar_agenda() # Executar função carregar_agenda
    if not agenda:
        print("Nenhuma tarefa na agenda.")
        return
    
    agora = datetime.now()
    lembretes_encontrados = False

    for tarefa in agenda:
#        if tarefa.lembrete  != "None" and agora <= tarefa.lembrete <= agora+timedelta(hours = 1):
        if tarefa.lembrete and agora <= tarefa.lembrete <= agora+timedelta(hours = 1):
            if not lembretes_encontrados:
                print("Seu(s) próximo(s) lembrete(s) é(são): ")
            print(f"Descrição: {tarefa.descricao}")
            print(f"Lembrete: {tarefa.lembrete.strftime('%d/%m/%Y %H:%M')}")
            print()
            lembretes_encontrados = True

    if not lembretes_encontrados:
        print("Nenhum lembrete progrmado para a próxima hora.")

# Loop principal do programa

while True:
    print(" --- Minha Agenda de Tarefas --- ")
    print(" 1. Adicionar tarefa ")
    print(" 2. Editar tarefa")
    print(" 3. Remover tarefa")
    print(" 4. Exibir tarefas pendentes")
    print(" 5. Verificar lembretes próximos")
    print(" 0. Sair")
    opcao = input(" Escolha o número de uma opção: ")
    print()

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        editar_tarefa()
    elif opcao == "3":
        remover_tarefa()
    elif opcao == "4":
        exibir_tarefas_pendentes()
    elif opcao == "5":
        verificar_lembretes_proximos()
    elif opcao == "0":
        print("Fim do programa.")
        break
    else:
        print("Opção inválida. Digite o número correspondente à opção desejada.")

    print()