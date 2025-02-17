import random
import time
import threading
from typing import List

class Tarefa:
    def __init__(self, id_tarefa: int, duracao: int):
        self.id_tarefa = id_tarefa
        self.duracao = duracao

    def executar(self):
        print(f"Executando job {self.id_tarefa} por {self.duracao} segundos...")
        time.sleep(self.duracao)
        print(f"Job {self.id_tarefa} concluído.")

class NoProcessamento:
    def __init__(self, id_no: int):
        self.id_no = id_no
        self.carga_atual = 0
        self.lock = threading.Lock()

    def executar_job(self, tarefa: Tarefa):
        with self.lock:
            self.carga_atual += tarefa.duracao

        def run():
            print(f"Tarefa {tarefa.id_tarefa} sendo executada no Nó {self.id_no}.")
            tarefa.executar()
            with self.lock:
                self.carga_atual -= tarefa.duracao

        thread = threading.Thread(target=run)
        thread.start()

class BalanceadorCluster:
    def __init__(self, nos: List[NoProcessamento]):
        self.nos = nos

    def obter_no_disponivel(self) -> NoProcessamento:
        return min(self.nos, key=lambda n: n.carga_atual)

    def balancear_job(self, tarefa: Tarefa):
        no = self.obter_no_disponivel()
        no.executar_job(tarefa)

# Simulação de processamento no cluster
nos_cluster = [NoProcessamento(id_no=i) for i in range(3)]
balanceador_cluster = BalanceadorCluster(nos_cluster)

jobs = [Tarefa(id_tarefa=i, duracao=random.randint(1, 10)) for i in range(6)]
for job in jobs:
    balanceador_cluster.balancear_job(job)