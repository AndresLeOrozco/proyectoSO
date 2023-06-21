# Definir la estructura del proceso (PCB)
class Process:
    def __init__(self, id, state, arrival_time, burst_time, priority, size):
        self.id = id
        self.state = state
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.size = size
        self.waiting_time = 0

 
    def __str__(self):
        return "ID: %i \n Tiempo de Rafaga: %ims \n Tiempo Restante: %ims \n Prioridad: %i \n Tiempo de Espera: %ims" % (self.id,self.burst_time,self.remaining_time,self.priority,self.waiting_time)