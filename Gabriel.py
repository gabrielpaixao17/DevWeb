import tkinter as tk

def evaluate(event):
    result_label.config(text=str(eval(entry.get())))

    root = tk.TK()
    root.title("Calculadora Simples")

    entry = tk.Entry(root)
    entry.bint("<Return>", evaluate)
    entry.pack()

    result_label = tk.label(root, text="")
    result_label.pack()

    root.geometry("250x100")
    root.mainloop()


    
