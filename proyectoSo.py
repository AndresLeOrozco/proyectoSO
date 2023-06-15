from GUI import *
import tkinter as tk
from CPUsimulation import *

if __name__ == '__main__':
    simulacion = CPUSimulation(4)
    simulacion.generate_process(12)
    simulacion.round_robin()
    print(simulacion.log)
