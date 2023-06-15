import time
from time import perf_counter, sleep
from threading import *
from datetime import datetime
from Process import *
from tkinter import messagebox, filedialog
from random import *
# Clase de la simulación
class CPUSimulation:
    def __init__(self,quant):
        self.new_queue = []  # Cola de procesos nuevos
        self.ready_queue = []  # Cola de procesos preparados
        self.waiting_queue = []  # Cola de procesos en espera
        self.end_process = []
        self.log = []  # Registro de cambios de contexto
        self.quantum = quant  # Quantum de tiempo de la CPU en ms
        self.context_switch_time = int(self.quantum * 0.1)  # Tiempo de cambio de contexto en ms
        self.io_interrupt_time = 5000  # Tiempo de interrupción de E/S en ms
        self.user_time = perf_counter() #Este es el tiempo que dura el usuario en elegir ingresar aqui
        
        

    # Este metodo es para crear cada uno de los procesos.
    def generate_process(self,cant):
        random.seed()
        id = 0
        for i in range (cant):
            process = Process(id,"Nuevo",0,random.uniform(1,10),random.uniform(1,5),random.uniform(1,100))
            self.new_queue.append(process)
            id += 1  

    # Aqui se van a sacar los procesos del new_queue para ingresarlo al ready_queue
    def prepare_process(self,tiempo_llegada):
        if len(self.ready_queue) <= 10:
            process = self.new_queue.pop(0)
            process.state = "Preparado"
            process.arrival_time = tiempo_llegada
            self.ready_queue.append(process)
            return True
        return False

    # Este es el metodo que interrumpe el proceso
    def inturruption_process(self):
        if self.ready_queue:
            # Primero registrar el cambio de contexto en el log
            self.context_switch()
            # Se registra el proceso y se saca del queue y cambiandole el estado
            process = self.ready_queue.pop(0)
            process.state = "En espera"
            self.waiting_queue.append(process)
            #Se define el tiempo que deberia esperar el proceso
            time.sleep(self.io_interrupt_time / 1000)
            process.state = "Preparado"
            self.ready_queue.append(process)


    def schedule_processes(self, algorithm):
        if algorithm == "Round Robin":
            self.round_robin()
        elif algorithm == "Prioridades con Round Robin":
            self.priority_round_robin()
        else:
            messagebox.showerror("Error", "Algoritmo desconocido")
    def round_robin(self):
        while self.new_queue or self.ready_queue:
            if len(self.ready_queue) < 10:
                tiempo_llegada = round(perf_counter() - self.user_time)
                while self.prepare_process(tiempo_llegada):
                    pass

            if self.ready_queue:
                process = self.ready_queue.pop(0)
                process.state = "Ejecutando"
                #Verificar si el tiempo de restante de la rafaga es mayor o menor al quantum menos el 10% de ese quantum
                if process.remaining_time <= self.quantum -  self.context_switch_time: 
                    time.sleep(process.remaining_time)
                    self.context_switch()
                    self.waiting_time += len(self.ready_queue) * process.remaining_time
                    process.remaining_time = 0
                    process.state = "Terminado"
                    self.finished_processes.append(process)
                else:
                    time.sleep(self.quantum - self.context_switch_time)
                    self.context_switch()
                    process.remaining_time -= self.quantum
                    self.ready_queue.append(process)

    def priority_round_robin(self):
        
        while  self.ready_queue:
            if self.new_queue:
                process = self.new_queue.pop(0)
                process.state = "Preparado"
                self.ready_queue.append(process)

            if self.ready_queue:
                self.ready_queue.sort(key=lambda x: x.priority)  # Ordenar por prioridad
                process = self.ready_queue.pop(0)
                process.state = "Ejecutando"

                if process.remaining_time <= self.quantum:
                    time.sleep(process.remaining_time / 1000)
                    self.context_switch()
                    process.remaining_time = 0
                    process.state = "Terminado"
                    self.finished_processes.append(process)
                else:
                    time.sleep(self.quantum / 1000)
                    self.context_switch()
                    process.remaining_time -= self.quantum
                    self.ready_queue.append(process)

    def context_switch(self):
        if len(self.ready_queue) > 1:
            time.sleep(self.context_switch_time)
            self.log.append(
                f"{datetime.now()}: Cambio de contexto - Proceso saliente: {self.ready_queue[0].id}, Proceso entrante: {self.ready_queue[1].id}")


    def calculate_waiting_time(self):
        for process in self.finished_processes:
            process.waiting_time = process.arrival_time
            for i in range(self.finished_processes.index(process)):
                process.waiting_time += self.finished_processes[i].burst_time

    def average_waiting_time(self):
        total_waiting_time = sum(process.waiting_time for process in self.finished_processes)
        return total_waiting_time / len(self.finished_processes)
    