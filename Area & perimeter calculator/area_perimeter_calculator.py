import tkinter as tk

def area():
    try:
        l = float(entry_l.get())
        b = float(entry_b.get())
        result = l * b
        result_label.config(text=f"Area = {result}")
    except ValueError:
        result_label.config(text="Invalid input")

def perimeter():
    try:
        l = float(entry_l.get())
        b = float(entry_b.get())
        result = 2 * (l + b)
        result_label.config(text=f"Perimeter = {result}")
    except ValueError:
        result_label.config(text="Invalid input")

window = tk.Tk()
window.title("Area & Perimeter Calculator")
window.geometry("300x200")

tk.Label(window, text="Enter Length:").pack()
entry_l = tk.Entry(window)
entry_l.pack()

tk.Label(window, text="Enter Breadth:").pack()
entry_b = tk.Entry(window)
entry_b.pack()

tk.Button(window, text="Calculate Area", command=area).pack(pady=5)
tk.Button(window, text="Calculate Perimeter", command=perimeter).pack()

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()