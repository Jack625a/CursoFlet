import tkinter as tk
from tkinter import messagebox
from scipy.optimize import linprog

def solve():
    try:
        # Obtener los coeficientes de la función objetivo
        c = list(map(float, entry_obj_func.get().split()))
        
        # Obtener los coeficientes de las restricciones
        A = []
        for entry in entry_restrictions:
            A.append(list(map(float, entry.get().split())))
        
        # Obtener los lados derechos de las restricciones
        b = list(map(float, entry_rhs.get().split()))

        # Negar los coeficientes de la función objetivo para maximizar
        c = [-coef for coef in c]
        
        # Resolver el problema de programación lineal
        res = linprog(c, A_ub=A, b_ub=b, method='simplex')

        if res.success:
            messagebox.showinfo("Resultado", f"Valor óptimo: {-res.fun}\nVariables de decisión: {res.x}")
        else:
            messagebox.showerror("Error", "No se encontró una solución óptima.")
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("Método Simplex")

# Crear los widgets
tk.Label(root, text="Coeficientes de la función objetivo (separados por espacio):").grid(row=0, column=0, padx=10, pady=10)
entry_obj_func = tk.Entry(root)
entry_obj_func.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Coeficientes de las restricciones (cada fila separada por enter):").grid(row=1, column=0, padx=10, pady=10)
frame_restrictions = tk.Frame(root)
frame_restrictions.grid(row=1, column=1, padx=10, pady=10)
entry_restrictions = [tk.Entry(frame_restrictions) for _ in range(3)]
for i, entry in enumerate(entry_restrictions):
    entry.grid(row=i, column=0, pady=2)

tk.Label(root, text="Lados derechos de las restricciones (separados por espacio):").grid(row=2, column=0, padx=10, pady=10)
entry_rhs = tk.Entry(root)
entry_rhs.grid(row=2, column=1, padx=10, pady=10)

btn_solve = tk.Button(root, text="Resolver", command=solve)
btn_solve.grid(row=3, column=0, columnspan=2, pady=10)

# Ejecutar la aplicación
root.mainloop()
