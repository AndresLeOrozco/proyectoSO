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
        
        self.label_quantity = tk.Label(root, text="Ingrese la cantidad de procesos en la simulacion:")
        self.process_quantity =  tk.Entry(root)
        self.label_quantum = tk.Label(root, text="Ingrese el tiempo del quantum:")
        self.process_quantum = tk.Entry(root)
        self.btn_start_simulation = tk.Button(root, text="Iniciar simulación", command=lambda:self.start_simulation())

        # Posicionar widgets
        self.label_algorithm.pack()
        self.combo_algorithm.pack()

        self.btn_start_simulation.pack()
        self.label_quantity.pack()
        self.process_quantity.pack()
        self.label_quantum.pack()
        self.process_quantum.pack()

    def start_simulation(self):
        quantum =  self.process_quantum.get()
        quantity = self.process_quantity.get()
        if quantum == "" or quantity  == "":
            messagebox.showerror("Error", "Debe rellenar todos los campos")
            return
        else:  
            simulacion = CPUSimulation(int(self.process_quantum.get()))
            simulacion.generate_process(int(self.process_quantity.get()))
            algorithm = self.selected_algorithm.get()
            if not algorithm:
                messagebox.showerror("Error", "Debe seleccionar un algoritmo")
                return
            if algorithm == "Round Robin":
                simulacion.round_robin()
            if algorithm == "Prioridades con Round Robin":
                simulacion.priority_round_robin()
            for i in simulacion.log:
                print(i)
                simulacion.geStaticts()
            simulacion.writeStatistics()
            messagebox.showinfo("Información", "Simulación finalizada")

