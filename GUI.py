import tkinter as tk
from tkinter import *
from CPUsimulation import *

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500")
        self.root.title("Simulación de Planificación de CPU")
        self.selected_algorithm = tk.StringVar()  # Variable de control para el algoritmo seleccionado

        # Crear widgets
        self.label_algorithm = tk.Label(root, text="Seleccione el algoritmo:")
        self.combo_algorithm = tk.OptionMenu(root, self.selected_algorithm, *["Round Robin", "Prioridades con Round Robin"])
        self.btn_start_simulation = tk.Button(root, text="Iniciar simulación", command=lambda:self.start_simulation())
        self.label_quantity = tk.Label(root, text="Ingrese la cantidad de procesos en la simulacion:")
        self.process_quantity =  tk.Entry(root)
        self.label_quantum = tk.Label(root, text="Ingrese el tiempo del quantum:")
        self.process_quantum = tk.Entry(root)

        # Posicionar widgets
        self.label_algorithm.pack()
        self.combo_algorithm.pack()

        self.btn_start_simulation.pack()
        self.label_quantity.pack()
        self.process_quantity.pack()
        self.label_quantum.pack()
        self.process_quantum.pack()

    def start_simulation(self):
        if self.process_quantum.get() or self.process_quantity.get() == "":
            
            return
        else:  
            simulacion = CPUSimulation(self.process_quantum.get())
            simulacion.generate_process(self.process_quantity.get())
            algorithm = self.selected_algorithm.get()
            if not algorithm:
                messagebox.showerror("Error", "Debe seleccionar un algoritmo")
                return
            if algorithm == "Round Robin":
                simulacion.round_robin()
            if algorithm == "Prioridades con Round Robin":
                simulacion.priority_round_robin()
            self.simulation.calculate_waiting_time()
            messagebox.showinfo("Información", "Simulación finalizada")

