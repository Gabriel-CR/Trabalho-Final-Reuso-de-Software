import random
import time
import threading

from typing import List

class Tarefa:
    def __init__(self, id_tarefa: int, duracao: int):
        self.id_tarefa = id_tarefa
        self.duracao = duracao

    def executar(self):
        print(f"Processando requisição {self.id_tarefa} por {self.duracao} segundos...")
        time.sleep(self.duracao)
        print(f"Requisição {self.id_tarefa} concluída.")

class Servidor:
    def __init__(self, nome: str):
        self.nome = nome
        self.carga_atual = 0
        self.lock = threading.Lock()

    def atribuir_requisicao(self, tarefa: Tarefa):
        with self.lock:
            self.carga_atual += tarefa.duracao

        def run():
            print(f"Requisição {tarefa.id_tarefa} atribuída ao {self.nome}.")
            tarefa.executar()
            with self.lock:
                self.carga_atual -= tarefa.duracao

        thread = threading.Thread(target=run)
        thread.start()

class BalanceadorDeServidores:
    def __init__(self, servidores: List[Servidor]):
        self.servidores = servidores

    def obter_servidor_menos_carregado(self) -> Servidor:
        return min(self.servidores, key=lambda s: s.carga_atual)

    def atribuir_requisicao(self, tarefa: Tarefa):
        servidor = self.obter_servidor_menos_carregado()
        servidor.atribuir_requisicao(tarefa)

# Simulação de requisições
servidores = [Servidor("Servidor A"), Servidor("Servidor B"), Servidor("Servidor C")]
balanceador = BalanceadorDeServidores(servidores)

requisicoes = [Tarefa(id_tarefa=i, duracao=random.randint(1, 10)) for i in range(5)]
for requisicao in requisicoes:
    balanceador.atribuir_requisicao(requisicao)