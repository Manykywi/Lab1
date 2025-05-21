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
        color = color_var.get()

        g = 9.81  # прискорення вільного падіння

        angle_rad = math.radians(angle_deg)
        vx0 = v0 * math.cos(angle_rad)
        vy0 = v0 * math.sin(angle_rad)

        # Час польоту до повернення на рівень y0 (або доки y >= 0)
        total_time = (vy0 + math.sqrt(vy0 ** 2 + 2 * g * y0)) / g if y0 > 0 else 2 * vy0 / g
        t = [i * 0.05 for i in range(int(total_time / 0.05) + 1)]

        x = [x0 + vx0 * ti for ti in t]
        y = [y0 + vy0 * ti - 0.5 * g * ti ** 2 for ti in t]

        # Відкидаємо всі точки, де y < 0
        x_filtered = []
        y_filtered = []
        for xi, yi in zip(x, y):
            if yi < 0:
                break
            x_filtered.append(xi)
            y_filtered.append(yi)

        plt.plot(x_filtered, y_filtered, color=color)

        if len(x_filtered) >= 2:
            dx = x_filtered[-1] - x_filtered[-2]
            dy = y_filtered[-1] - y_filtered[-2]
            plt.arrow(x_filtered[-2], y_filtered[-2], dx, dy, head_width=0.3, head_length=0.4, fc=color, ec=color)

        plt.title("Траєкторія руху (під дією тяжіння)")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.axis("equal")
        plt.show()

    except Exception as e:
        print("Помилка:", e)

# Інтерфейс
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
entry_v0.insert(0, "10")

tk.Label(root, text="Колір траєкторії:").grid(row=4, column=0, sticky="e")
color_var = tk.StringVar(value="red")
ttk.Combobox(root, textvariable=color_var, values=["red", "blue", "green", "purple", "black"]).grid(row=4, column=1)

tk.Button(root, text="Побудувати графік", command=plot_trajectory).grid(row=5, columnspan=2, pady=10)

root.mainloop()
