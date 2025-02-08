import random
import time
from typing import List

class Tarefa:
    def __init__(self, id_tarefa: int, duracao: int):
        self.id_tarefa = id_tarefa
        self.duracao = duracao

    def executar(self):
        print(f"Executando a Tarefa {self.id_tarefa} por {self.duracao} segundos...")
        time.sleep(self.duracao)
        print(f"Tarefa {self.id_tarefa} concluída.")

class Componente:
    def __init__(self, nome: str):
        self.nome = nome
        self.carga_atual = 0

    def atribuir_tarefa(self, tarefa: Tarefa):
        print(f"Tarefa {tarefa.id_tarefa} atribuída ao {self.nome}.")
        self.carga_atual += tarefa.duracao
        tarefa.executar()
        self.carga_atual -= tarefa.duracao

class BalanceadorDeTarefas:
    def __init__(self, componentes: List[Componente]):
        self.componentes = componentes

    def obter_componente_menos_carregado(self) -> Componente:
        return min(self.componentes, key=lambda c: c.carga_atual)

    def atribuir_tarefa(self, tarefa: Tarefa):
        componente = self.obter_componente_menos_carregado()
        componente.atribuir_tarefa(tarefa)

# Exemplo de uso
if __name__ == "__main__":
    componentes = [
        Componente("Componente A"),
        Componente("Componente B"),
        Componente("Componente C")
    ]
    
    balanceador = BalanceadorDeTarefas(componentes)

    # Criação de tarefas simuladas
    tarefas = [Tarefa(id_tarefa=i, duracao=random.randint(1, 3)) for i in range(5)]

    # Atribuição balanceada de tarefas
    for tarefa in tarefas:
        balanceador.atribuir_tarefa(tarefa)