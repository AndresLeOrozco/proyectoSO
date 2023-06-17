from GUI import *
import tkinter as tk
from CPUsimulation import *

if __name__ == '__main__':
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
    # simulacion = CPUSimulation(3)
    # simulacion.generate_process(14)
    # simulacion.priority_round_robin()
    # for i in simulacion.log:
    #     print(i)
    # simulacion.geStaticts()


