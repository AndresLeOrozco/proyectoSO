# Definir la estructura del proceso (PCB)
class Process:
    def __init__(self, pid, state, arrival_time, burst_time, priority, size):
        self.pid = pid
        self.state = state
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.size = size
