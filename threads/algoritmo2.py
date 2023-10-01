import threading
import time

chave_a = 0 
chave_b = 0

def processo_a():
    global chave_a, chave_b
    
    for _ in range(2):
        print("Início do Processo A")
        while chave_b !=0 :
            print("Processo A em Espera Ocupada")
        
        chave_a = 1

        for _ in range(3):
            print("Região Critica de A")

        chave_a = 0

        for _ in range(3):
            print("Região NÃO Critica de A")
            time.sleep(0.01)


def processo_b():
   global chave_a, chave_b

   for _ in range(2):
        print("Início do Processo B")

        while chave_a != 1 :
            print("Processo B em Espera Ocupada")
    
        chave_b = 1

        for _ in range(3):
            print("Região Critica de B")
        
        chave_b = 0
        

        for _ in range(3):
            print("Região NÃO Critica de B")


thread1 = threading.Thread(target=processo_a)
thread2 = threading.Thread(target=processo_b)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Ambas as tarefas foram concluídas")