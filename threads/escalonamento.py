import threading
import time

def FirstTask():
    print("Início da Tarefa 1")
    for _ in range(5):
        print("Tarefa 1 executando")
        time.sleep(1.6)
    print("Fim da Tarefa 1")

def SecondTask():
    print("Início da Tarefa 2")
    for _ in range(5):
        print("Tarefa 2 executando")
        time.sleep(0.8)
    print("Fim da Tarefa 2")

thread1 = threading.Thread(target=FirstTask)
thread2 = threading.Thread(target=SecondTask)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Ambas as tarefas foram concluídas")