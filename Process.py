# Definir la estructura del proceso (PCB)
class Process:
    def __init__(self, id, state, arrival_time, burst_time, priority, size):
        self.id = id
        self.state = state
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = 0
        self.priority = priority
        self.size = size

 
