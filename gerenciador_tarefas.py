class Tarefa:
    def __init__(self, nome, descricao=None, status='Pendente'):
        self.nome = nome
        self.descricao = descricao
        self.status = status
        self.concluida = False


class GerenciadorTarefa:
    def __init__(self):
        self.lista_tarefas = []
        self.carregar_tarefas_do_arquivo()


    def linhas(self):
        print('-=' * 40)


    def carregar_tarefas_do_arquivo(self):
        """Carrega as tarefas salvas no arquivo evitando duplicações"""
        try:
            with open('Tarefas.txt', 'r', encoding='utf-8') as arquivo:
                for linha in arquivo:
                    if linha.startswith('Tarefa'):
                        partes = linha.strip().split(' - ')
                        nome_tarefa = partes[0].split(':', 1)[1].strip()
                        descricao = (
                            partes[1].strip() if len(partes) > 2 else None
                        )
                        status = (
                            partes[2].strip() if len(partes) > 2 else 'Pendente'
                        )
                        if (
                            nome_tarefa
                            not in [tarefa.nome for tarefa in self.lista_tarefas]
                        ):
                            nova_tarefa = Tarefa(nome_tarefa, descricao, status)
                            self.lista_tarefas.append(nova_tarefa)
        except FileNotFoundError:
            print('Arquivo de tarefas não encontrado criando um novo... ')


    def salvar_tarefas_no_arquivo(self):
        """Salva as tarefas no arquivo Tarefas.txt"""
        with open('Tarefas.txt', 'w', encoding='utf-8') as arquivo:
            for tarefa in self.lista_tarefas:
                descricao = tarefa.descricao if tarefa.descricao else ''
                arquivo.write(
                    f'Tarefa: {tarefa.nome} - {descricao} - {tarefa.status}\n'
                )


    def adicionar_tarefa(self):
        """Adicionar tarefa a lista de tarefas"""
        while True:
            self.linhas()

            nome_tarefa = (
                input(f'Qual tarefa você vai adicionar a lista: ')
                .strip()
                .lower()
            )
            if nome_tarefa != 'nenhuma':
                descricao = None            
                if nome_tarefa  not in[tarefa.nome for tarefa in self.lista_tarefas]:
                    descricao_opcional = (
                        input('\033[34mDESCRIÇÃO\033[0m: Você deseja adicionar '
                              'uma descrição? (Opcional) [Sim/Não]: ')
                              .strip()
                              .lower()
                    )
                    if descricao_opcional == 'sim':
                        descricao = input('Descrição: ').strip().lower()
                    nova_tarefa = Tarefa(nome_tarefa, descricao)
                    self.lista_tarefas.append(nova_tarefa)
                    print(f'Tarefa "{nome_tarefa}" adicionada com sucesso. ')

                    self.salvar_tarefas_no_arquivo()
                    
                    with open('Tarefas.txt', 'a', encoding='utf-8') as arquivo:
                        arquivo.write(
                            f'Tarefa: {nova_tarefa.nome} - '
                            f'{nova_tarefa.descricao} - {nova_tarefa.status}\n')
                else:
                     print('Tarefa já está na lista de tarefas. ')
                finalizar = (
                    input('\033[32mADICIONAR\033[0m: Você deseja adicionar '  
                          'outra tarefa? [Sim/Não]: ')
                          .strip()
                          .lower()
                )
                if finalizar in ['não', 'nao']:
                    break
                elif finalizar == 'sim':
                    continue
                elif finalizar != 'sim':
                    print('\033[31mERRO\033[0m: Opção invalída. ')
            break      


    def remover_tarefa(self):
        """Úsuario remove uma tarefa (caso ele queira) do arquivo Tarefas.txt"""
        opcao = (
            input('\033[33mREMOVER\033[0m: Você deseja remover alguma tarefa? ' 
                  '[Sim/Não]: ').strip().lower()
        )
        if opcao == 'sim':
            tarefa_a_remover = (
                input('Digite o nome ou ID da tarefa que você deseja remover: ')
                .strip()
                .lower()
            )
            try:
                indice = int(tarefa_a_remover)
                if 1 <= indice <= len(self.lista_tarefas):
                    tarefa_removida = self.lista_tarefas.pop(indice-1)
                    print(f'Tarefa {tarefa_removida.nome} removida com sucesso.')
                    self.salvar_tarefas_no_arquivo()
                else:
                    print(
                        f'\033[31mERRO\033[0m: Não existe uma tarefa '
                        f'com o número {indice} na lista.')
            except ValueError:    
                for tarefa in self.lista_tarefas:
                    if tarefa.nome == tarefa_a_remover:    
                        self.lista_tarefas.remove(tarefa)
                        print(f'Tarefa {tarefa_a_remover} removida com sucesso.')
                        self.salvar_tarefas_no_arquivo()
                        return        
                print(
                    f'\033[31mErro\033[0m: A tarefa {tarefa_a_remover}' 
                    'não foi encontrada na lista. ')
        elif opcao not in ['não', 'nao']:
            print('\033[31mErro\033[0m: Opção invalída. ')


    def exibir_tarefas(self):
        """Exibir as tarefas"""
        self.linhas()
        if not self.lista_tarefas:
            print('Nenhuma tarefa na lista')
        else:
            print('Suas tarefas são: ')
            for i, tarefa in enumerate(self.lista_tarefas, start=1):
                self.status = (
                    'Concluída' if tarefa.concluida else 'Não concluída'
                )
                descricao = f'- {tarefa.descricao}' if tarefa.descricao else ''
                print(
                    f'{i} - {tarefa.nome} {descricao} - Status: {tarefa.status}'
                ) 
        self.linhas()


    def marcar_como_concluida(self):
        """Marcar as tarefas como concluídas"""
        tarefa_concluida = (
            input('Digite o nome da tarefa que você já concluíu: ')
            .strip()
            .lower()
        )
        
        if tarefa_concluida != 'nenhuma':
            for tarefa in self.lista_tarefas:
                if tarefa.nome.lower() == tarefa_concluida:
                    if not tarefa.concluida:
                        tarefa.concluida = True
                        tarefa.status = 'Concluída'
                        print(
                            f'Tarefa {tarefa_concluida} marcada como concluída.'
                        )
                        self.salvar_tarefas_no_arquivo()
                        return
                    else:
                        print(
                            f'Tarefa {tarefa_concluida}'
                             'já está marcada como concluída. '
                        )
                        return


"""
gerenciador = GerenciadorTarefa()
gerenciador.adicionar_tarefa()
gerenciador.remover_tarefa()
gerenciador.exibir_tarefas()
gerenciador.marcar_como_concluida()
gerenciador.exibir_tarefas()
"""