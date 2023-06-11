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

    def load_processes(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                for line in file:
                    process_info = line.strip().split(",")
                    pid = process_info[0]
                    state = "Nuevo"
                    arrival_time = int(process_info[1])
                    burst_time = int(process_info[2])
                    priority = int(process_info[3])
                    size = int(process_info[4])
                    self.simulation.add_process(pid, state, arrival_time, burst_time, priority, size)
            messagebox.showinfo("Información", "Procesos cargados exitosamente")

    def start_simulation(self):
        algorithm = self.selected_algorithm.get()
        if not algorithm:
            messagebox.showerror("Error", "Debe seleccionar un algoritmo")
            return
        self.simulation.schedule_processes(algorithm)
        self.simulation.calculate_waiting_time()
        messagebox.showinfo("Información", "Simulación finalizada")

    def io_interrupt(self):
        self.simulation.io_interrupt()
        messagebox.showinfo("Información", "Interrupción de E/S aplicada")

    def finish_simulation(self):
        average_waiting_time = self.simulation.average_waiting_time()
        messagebox.showinfo("Información", f"Tiempo de espera promedio: {average_waiting_time}")

        log_file_path = filedialog.asksaveasfilename(filetypes=[("Archivos de texto", "*.txt")])
        if log_file_path:
            with open(log_file_path, "w") as file:
                for log_entry in self.simulation.log:
                    file.write(log_entry + "\n")
            messagebox.showinfo("Información", "Bitácora guardada exitosamente")
