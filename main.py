from gerenciador_tarefas import Tarefa, GerenciadorTarefa

if __name__ == '__main__':
    gerenciador = GerenciadorTarefa()
    gerenciador.adicionar_tarefa()  
    gerenciador.remover_tarefa()
    gerenciador.exibir_tarefas()
    gerenciador.marcar_como_concluida()
    gerenciador.exibir_tarefas()
