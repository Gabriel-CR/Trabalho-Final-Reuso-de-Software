import random
import time
import threading
from typing import List

class Tarefa:
    def __init__(self, id_tarefa: int, duracao: int):
        self.id_tarefa = id_tarefa
        self.duracao = duracao

    def executar(self):
        print(f"Processando tarefa {self.id_tarefa} por {self.duracao} segundos...")
        time.sleep(self.duracao)
        print(f"Tarefa {self.id_tarefa} concluída.")

class Maquina:
    def __init__(self, nome: str):
        self.nome = nome
        self.carga_atual = 0
        self.lock = threading.Lock()

    def processar_tarefa(self, tarefa: Tarefa):
        with self.lock:
            self.carga_atual += tarefa.duracao

        def run():
            print(f"Tarefa {tarefa.id_tarefa} sendo executada na {self.nome}.")
            tarefa.executar()
            with self.lock:
                self.carga_atual -= tarefa.duracao

        thread = threading.Thread(target=run)
        thread.start()

class BalanceadorDeMaquinas:
    def __init__(self, maquinas: List[Maquina]):
        self.maquinas = maquinas

    def obter_maquina_disponivel(self) -> Maquina:
        return min(self.maquinas, key=lambda m: m.carga_atual)

    def distribuir_tarefa(self, tarefa: Tarefa):
        maquina = self.obter_maquina_disponivel()
        maquina.processar_tarefa(tarefa)

# Simulação de tarefas na linha de produção
maquinas = [Maquina("Máquina 1"), Maquina("Máquina 2"), Maquina("Máquina 3")]
balanceador = BalanceadorDeMaquinas(maquinas)

tarefas_producao = [Tarefa(id_tarefa=i, duracao=random.randint(1, 10)) for i in range(4)]
for tarefa in tarefas_producao:
    balanceador.distribuir_tarefa(tarefa)