tarefas = []  # Lista onde serão armazenadas as tarefas

# Menu de opções
print('Escolha uma opção:')
print('1- Adicionar Tarefa')
print('2- Ver lista de tarefas')
print('3- Gerar arquivo txt')
print('4- Sair')

ativo = True  # Flag para manter o loop ativo

while ativo:
    escolha = input("Escolha uma opção: ")  # Input principal do menu
    
    if escolha == '4':
        print('Encerrando')  # Mensagem de encerramento
        ativo = False  # Encerra o loop
        
    elif escolha == '1':
        # Adiciona uma nova tarefa à lista
        objetivo = input('Escolha o que você quer fazer: ').title()
        hora = input("Escreva que horas começa: ")
        tarefas.append({'objetivo': objetivo, 'hora': hora})
        print('Adicionado!')
        
    elif escolha == '2':
        # Mostra todas as tarefas cadastradas
        print('\n------------Lista de Tarefas---------')
        for tarefa in tarefas:
            print(f"Tarefa: {tarefa['objetivo']} | Horário de Início: {tarefa['hora']}")
            print('\n------------------------')
            
    elif escolha == '3':
        # Gera um arquivo .txt com as tarefas
        nome_arquivo = input('Digite o nome do arquivo para salvar: ') + '.txt'
        try:
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                arquivo.write('--------------Lista de Tarefas---------\n\n')
                for i, tarefa in enumerate(tarefas, 1):
                    arquivo.write(f'Tarefa {i}:\n')
                    arquivo.write(f'Descrição: {tarefa["objetivo"]}\n')
                    arquivo.write(f'Horário: {tarefa["hora"]}\n')
                    arquivo.write('\n')
                arquivo.write('------------------------------\n')
            print(f'Arquivo "{nome_arquivo}" gerado com sucesso!')
        except Exception as e:
            print(f"Erro ao gerar arquivo: {e}")
    
    else:
        print("Opção inválida. Tente novamente")
