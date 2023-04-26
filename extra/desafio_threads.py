import threading
import time


def tarefa1():
    for i in range(5):
        print(f"Executando tarefa 1 - Iteração {i + 1}")
        time.sleep(1)


def tarefa2():
    for i in range(5):
        print(f"Executando tarefa 2 - Iteração {i + 1}")
        time.sleep(1)


thread1 = threading.Thread(target=tarefa1)
thread2 = threading.Thread(target=tarefa2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Todas as tarefas foram concluídas.")
