import tkinter as tk
from tkinter import messagebox, filedialog
from CPUsimulation import *

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulación de Planificación de CPU")
        self.simulation = CPUSimulation()
        self.selected_algorithm = tk.StringVar()  # Variable de control para el algoritmo seleccionado

        # Crear widgets
        self.label_algorithm = tk.Label(root, text="Seleccione el algoritmo:")
        self.combo_algorithm = tk.OptionMenu(root, self.selected_algorithm, *["Round Robin", "Prioridades con Round Robin"])
        self.btn_load_processes = tk.Button(root, text="Cargar procesos", command=self.load_processes)
        self.btn_start_simulation = tk.Button(root, text="Iniciar simulación", command=self.start_simulation)
        self.btn_interrupt = tk.Button(root, text="Interrupción de E/S", command=self.io_interrupt)
        self.btn_finish_simulation = tk.Button(root, text="Finalizar simulación", command=self.finish_simulation)

        # Posicionar widgets
        self.label_algorithm.pack()
        self.combo_algorithm.pack()
        self.btn_load_processes.pack()
        self.btn_start_simulation.pack()
        self.btn_interrupt.pack()
        self.btn_finish_simulation.pack()

    

    def start_simulation(self):
        algorithm = self.selected_algorithm.get()
        if not algorithm:
            messagebox.showerror("Error", "Debe seleccionar un algoritmo")
            return
        self.simulation.schedule_processes(algorithm)
        self.simulation.calculate_waiting_time()
        messagebox.showinfo("Información", "Simulación finalizada")

