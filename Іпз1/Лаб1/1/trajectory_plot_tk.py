import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import math

def plot_trajectory():
    try:
        x0 = float(entry_x0.get())
        y0 = float(entry_y0.get())
        angle_deg = float(entry_angle.get())
        v0 = float(entry_v0.get())
        a = float(entry_a.get())
        color = color_var.get()

        angle_rad = math.radians(angle_deg)
        vx0 = v0 * math.cos(angle_rad)
        vy0 = v0 * math.sin(angle_rad)

        t = [i * 0.1 for i in range(100)]
        x = [x0 + vx0 * ti + (a * math.cos(angle_rad)) * (ti ** 2) / 2 for ti in t]
        y = [y0 + vy0 * ti + (a * math.sin(angle_rad)) * (ti ** 2) / 2 for ti in t]

        plt.plot(x, y, color=color)  # Лінія без крапочок

        # Стрілка в кінці траєкторії
        if len(x) >= 2:
            dx = x[-1] - x[-2]
            dy = y[-1] - y[-2]
            plt.arrow(x[-2], y[-2], dx, dy, head_width=0.3, head_length=0.4, fc=color, ec=color)

        plt.title("Траєкторія руху")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.axis("equal")  # Збереження масштабу осей
        plt.show()

    except Exception as e:
        print("Помилка:", e)

# Створення інтерфейсу
root = tk.Tk()
root.title("Траєкторія руху точки")

tk.Label(root, text="x0:").grid(row=0, column=0, sticky="e")
entry_x0 = tk.Entry(root)
entry_x0.grid(row=0, column=1)
entry_x0.insert(0, "0")

tk.Label(root, text="y0:").grid(row=1, column=0, sticky="e")
entry_y0 = tk.Entry(root)
entry_y0.grid(row=1, column=1)
entry_y0.insert(0, "0")

tk.Label(root, text="Кут (град):").grid(row=2, column=0, sticky="e")
entry_angle = tk.Entry(root)
entry_angle.grid(row=2, column=1)
entry_angle.insert(0, "45")

tk.Label(root, text="Початкова швидкість:").grid(row=3, column=0, sticky="e")
entry_v0 = tk.Entry(root)
entry_v0.grid(row=3, column=1)
entry_v0.insert(0, "5")

tk.Label(root, text="Прискорення:").grid(row=4, column=0, sticky="e")
entry_a = tk.Entry(root)
entry_a.grid(row=4, column=1)
entry_a.insert(0, "1")

tk.Label(root, text="Колір траєкторії:").grid(row=5, column=0, sticky="e")
color_var = tk.StringVar(value="red")
ttk.Combobox(root, textvariable=color_var, values=["red", "blue", "green", "purple", "black"]).grid(row=5, column=1)

tk.Button(root, text="Побудувати графік", command=plot_trajectory).grid(row=6, columnspan=2, pady=10)

root.mainloop()
