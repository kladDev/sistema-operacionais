import threading
import time

chave = 0

def tarefa1():
    global chave
    while(True):

        while(chave != 0):
            print("Espera ocupada 1")
            time.sleep(1)

        print("Região crítica de 1")
        time.sleep(0.5)
        chave = 1
        print("Região não-crítica de 1") 

def tarefa2():
    global chave
    while(True):

        while(chave != 1):
            print("Espera ocupada de 2")
            time.sleep(2)

        print("Região crítica de 2")
        time.sleep(0.2)
        chave = 0
        print("Região não-crítica de 2")

thread1 = threading.Thread(target=tarefa1)
thread2 = threading.Thread(target=tarefa2)


thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Ambas as tarefas foram concluídas")