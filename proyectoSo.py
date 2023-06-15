# from GUI import *
# import tkinter as tk
# from CPUsimulation import *

# if __name__ == '__main__':
#     root = tk.Tk()
#     gui = GUI(root)
#     root.mainloop()

from time import perf_counter, sleep


def tiempo():
   
    for r in range(5): 
        sleep(2)

    return perf_counter()


def tiempo2():

    for r in range(5): 
        sleep(2)

    return perf_counter()



end = perf_counter()

print(tiempo())
print(tiempo2())
print(perf_counter())