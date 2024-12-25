from datetime import datetime
import sqlite3

class GerenciadorTarefa:
    def __init__(self):
        self.conexao = sqlite3.connect('tarefas.db')
        self.cursor = self.conexao.cursor()
        self.criar_tabela()


    def criar_tabela(self):
        """Criar a tabela de tarefas no banco de dados"""
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS tarefas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    descricao TEXT,
                    status TEXT NOT NULL DEFAULT 'Pendente'            
                )
        ''')
        self.conexao.commit()


    def adicionar_tarefa(self, nome, descricao=None):
        """Adicionar uma tarefa no banco de dados"""
        self.cursor.execute('''
            INSERT INTO tarefas (nome, descricao) VALUES (?, ?)
        ''', (nome, descricao))
        self.conexao.commit()
        print(f'Tarefa "{nome}" adicionada com sucesso.')


    def listar_tarefas(self):
        """"Lista todas as tarefas do banco de dados"""
        self.cursor.execute('SELECT id, nome, descricao, status FROM tarefas')
        tarefas = self.cursor.fetchall()

        if not tarefas:
            print('Nenhuma tarefa encontrada. ')
        else:
            print('Suas tarefas: ')
            for tarefa in tarefas:
                id_tarefa, nome, descricao, status = tarefa
                descricao = descricao if descricao else 'Tarefa sem descrição'
                print(
                    f'ID: {id_tarefa} - Nome: {nome} - Descrição: {descricao}'
                    f'Status: {status}'
                )

    def remover_tarefa(self, id_tarefa):
        """Remove uma tarefa do banco de dados pelo ID"""
        self.cursor.execute('DELETE FROM tarefas WHERE id = ?', (id_tarefa,))
        self.conexao.commit()

        if self.cursor.rowcount > 0:
            print(f'Tarefa ID: {id_tarefa} removida com sucesso. ')
        else:
            print(f'Erro: Tarefa ID {id_tarefa} não encontrada. ')
    

    def marcar_como_concluida(self, id_tarefa):
        """Marcar uma tarefaa como concluída no banco de dados"""
        self.cursor.execute('''
            UPDATE tarefas
            SET status = 'Concluída'
            WHERE id = ? AND status != 'Concluída'
        ''', (id_tarefa,))
        self.conexao.commit()

        if self.cursor.rowcount > 0:
            print(f'Tarefa ID {id_tarefa} marcada como concluída')
        else:
            print(f'Erro: Tarefa ID {id_tarefa} não encontrada ou já concluída.')

    def fechar_conexao(self):
        """Fechar a conexão com o banco de dados"""
        self.conexao.close()
        