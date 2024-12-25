from gerenciador_tarefas import GerenciadorTarefa

if __name__ == '__main__':
    gerenciador = GerenciadorTarefa()
    
    while True:
        print('\nMenu de gerenciamento de tarefas:')
        print('1. Adicionar tarefa')
        print('2. Listar tarefas')
        print('3. Remover tarefa')
        print('4. Marcar tarefa como concluída')
        print('5. Sair')

        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            nome = input('Nome da tarefa: ').strip()
            descricao = input('Descrição da tarefa (Opcional): ').strip() or None
            gerenciador.adicionar_tarefa(nome, descricao)
        elif opcao == '2':
            gerenciador.listar_tarefas()
        elif opcao == '3':
            try:
                id_tarefa = int(input('ID da tarefa a remover: ').strip())
                gerenciador.remover_tarefa(id_tarefa)
            except ValueError:
                print('Erro o ID deve ser um número inteiro. ')
        elif opcao == '4':
            try:
                id_tarefa = int(input('ID da tarefa a ser marcada como concluída '))
                gerenciador.marcar_como_concluida(id_tarefa)
            except ValueError:
                print('Erro o ID deve ser um número inteiro. ')
        elif opcao == '5':
            gerenciador.fechar_conexao()
            print('Saindo do programa. Até logo! ')
            break
        else:
            print('\033[31mErro\033[0m: Opção invalída. Tente novamente. ')